import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
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
from collections import defaultdict
d = defaultdict(int)
for i in range(2, n+1):
    dd = factor(i)
    for k,v in dd.items():
        d[k] += dd[k]
n74 = sum(v>=74 for v in d.values())
n2 = sum(v>=2 for v in d.values())
n24 = sum(v>=24 for v in d.values())
n14 = sum(v>=14 for v in d.values())
n4 = sum(v>=4 for v in d.values())
ans = n74 + (n2-1)*n24 + (n4-1)*n14 + (n4*(n4-1)//2 * (n2-2) if n4>=1 else 0)
print(ans)