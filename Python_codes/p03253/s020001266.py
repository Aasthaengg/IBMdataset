N,M = map(int,input().split())
mod = 10**9+7
import collections 
# 素因数分解：Counter型で提出
def is_prime(n):
    ans = []
    for i in range(2,int(n**0.5)+1):
        while not n%i:
            n //= i
            ans.append(i)
    if n !=1:
        ans.append(n)
    return collections.Counter(ans)

#重複組み合わせ
def comb(v):
    ans = 1
    for i in range(1,v+1):
        ans *= N+i-1
        ans *= pow(i,mod-2,mod)
        ans %= mod
    return ans

ans = 1
for v in is_prime(M).values():
    ans *= comb(v)
    ans %= mod
print(ans)