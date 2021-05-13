from collections import defaultdict

n = int(input())
ans = 10**12
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        x, y = i, n // i
        ans = min(ans, x + y - 2)
print(ans)
