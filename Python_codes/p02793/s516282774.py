n = int(input())
a = list(map(int,input().split()))
d = {}
ans = 0
mod = 10**9 + 7

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

for i in a:
    arr = factorization(i)
    for j,k in arr:
        if j not in d:
            d[j] = k
        else:
            d[j] = max(k, d[j])

l = 1
for k,v in d.items():
    l *= pow(k,v,mod)
    l %= mod

for i in a:
    ans += l * pow(i, mod-2, mod)
    ans %= mod

print(ans)
