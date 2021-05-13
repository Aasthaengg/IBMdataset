import math

N, M = map(int, input().split())
Q = int(1e9 + 7)

if max(N, M) - min(N, M) > 1:
    print(0)
else:
    if N == M:
        ans = math.factorial(N)
        ans %= Q
        ans *= math.factorial(M)
        ans %= Q
        ans *= 2
        ans %= Q
    else:
        ans = math.factorial(N)
        ans %= Q
        ans *= math.factorial(M)
        ans %= Q
    print(ans)