def factorial(x, mod=10**9+7):
    v = 1
    for i in range(2, x+1):
        v *= i
        v %= mod
    return v


N, M = map(int, input().split())

if abs(N-M) > 1:
    print(0)
    exit()

mod = 10**9 + 7
if N == M:
    ans = (factorial(N) * factorial(M) * 2) % mod
else:
    ans = (factorial(N) * factorial(M)) % mod

print(ans)