import math

N, D = map(int, input().split())

ans = 0
for _ in range(N):
    X, Y = map(int, input().split())
    d =  math.sqrt(X**2 + Y**2)
    if d <= D:
        ans += 1
print(ans)