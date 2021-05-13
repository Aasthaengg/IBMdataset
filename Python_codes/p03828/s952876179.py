import collections as col

def prime(n):
    ans = []
    num = n
    for i in range(2,int(n**0.5)+1):
        if i%2==0 and i!=2: continue
        while num%i == 0: num //= i ; ans.append(i)
    if num != 1: ans.append(num)
    return ans

n = int(input())
mod = 10**9 + 7

primes = []
for i in range(2,n+1): primes += prime(i)

cnt = col.Counter(primes)
ans = 1
for key,val in cnt.items(): ans *= (val + 1) ; ans %= mod
print(ans)
