import math
N, M = map(int, input().split())

if abs(N - M) >= 2:
    ans = 0

elif N == M:
    ans = 2 * math.factorial(N) * math.factorial(M)

elif abs(N - M) == 1:
    ans = math.factorial(N) * math.factorial(M)

print(ans % (10**9 + 7))