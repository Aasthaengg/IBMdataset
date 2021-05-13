
N = int(input())

isPrime = [True]*(N+1)

isPrime[0] = False
isPrime[1] = False

for i in range(2, N + 1):
    if isPrime[i]:
        for j in range(2*i, N + 1, i):
            isPrime[j] = False


factors = []

for p in range(2, N+1):
    if not isPrime[p]:
        continue

    f = 0
    base = p
    while base <= N:
        f += N // base
        base *= p

    if f > 0:
        factors.append(f)

ans = 1
m = 10**9 + 7
for f in factors:
    ans *= (f+1)
    if ans >= m:
        ans %= m

print(ans)
