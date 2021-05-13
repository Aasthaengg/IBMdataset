import math

N, D = map(int, input().split())

cnt = 0
for _ in range(N):
    x, y = map(int, input().split())
    d = math.sqrt(x * x + y * y)
    if d <= D:
        cnt += 1

print(cnt)