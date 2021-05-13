n = int(input())
def factorize(n):
    b = 2
    fct = [(1,1)]
    while b * b <= n:
        cnt =0
        while n % b == 0:
            n //= b
            cnt +=1
        if cnt >=1:
            fct.append((b,cnt))
        b = b + 1
    if n > 1:
        fct.append((n,1))
    return fct

primes = [0]*(n+1)
for i in range(1,n+1):
    for num,cnt in factorize(i):
        if num==1:continue
        primes[num] +=cnt
ans = 1
mod = 10**9+7
for cnt in primes:
    ans = ans*(cnt+1)%mod
print(ans)
