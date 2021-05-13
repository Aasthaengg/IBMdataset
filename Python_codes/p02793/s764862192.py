from collections import Counter
MOD = 10**9+7
N = int(input())
A = list(map(int,input().split()))
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
prime = [0] * (10**6+1)
for i in range(N):
    c = Counter(prime_factorize(A[i]))
    for j in c.items():
        prime[j[0]] = max(j[1],prime[j[0]])
lcm = 1
for i in range(10**6):
    if prime[i] > 0:
        lcm *= pow(i,prime[i])
        lcm %= MOD

ans = 0
for i in range(N):
    ans += lcm * pow(A[i],MOD-2,MOD)
    ans %= MOD
print(ans)
