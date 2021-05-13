import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")

n = int(input())
a = list(map(int, input().split()))
M = 10**9+7

def factor(n, m=None):
    # mを与えると、高々その素因数まで見て、残りは分解せずにそのまま出力する
    arr = {}
    temp = n
    M = int(-(-n**0.5//1))+1
    if m is not None:
        M = min(m+1, M)
    for i in range(2, M):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr[i] = cnt

    if temp!=1:
        arr[temp] = 1

    if not arr:
        arr[n] = 1

    return arr

ds = [factor(num) for num in a]
D = {}
for d in ds:
    for k,v in d.items():
        if k in D:
            D[k] = max(D[k], v)
        else:
            D[k] = v
l = 1
for k,v in D.items():
    l *= pow(k,v,M)
    l %= M
ans = 0
for num in a:
    ans += (l*pow(num, M-2, M))
    ans %= M
print(ans)