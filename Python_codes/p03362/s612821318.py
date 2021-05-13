def sieve(n):
    isPrime = [True]*(n+1)
    isPrime[0] = isPrime[1] = False
    for i in range(3,n+1,2):
        if isPrime[i]:
            for j in range(2*i,n+1,i): isPrime[j] = False
    for i in range(4,n+1,2): isPrime[i] = False
    return isPrime

n = int(input())
ans = []
for i,p in enumerate(sieve(55555)):
    if p and i%5 == 1:
        ans.append(i)
        if len(ans) == n: break
print(*ans)