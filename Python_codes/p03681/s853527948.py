import math

N, M = map(int, input().split())
if N == M:
    ans = (math.factorial(N) ** 2) * 2
elif abs(N - M) == 1:
    x = max(N, M)
    ans = (math.factorial(x) ** 2) // x
else:
    ans = 0
print(ans % (10 ** 9 + 7))
