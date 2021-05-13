import math
n, d = list(map(int, input().split()))

ans = 0
for _ in range(n):
    x, y = list(map(int, input().split()))
    dist = math.sqrt(x ** 2 + y ** 2)
    if dist <= d:
        ans += 1
print(ans)