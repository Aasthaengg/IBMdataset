import math

n, k = list(map(int, input().split()))
h = [int(input()) for _ in range(n)]
h.sort()
ans = math.inf
for i in range(n - k + 1):
    ans = min(ans, h[i + k - 1] - h[i])

print(ans)
