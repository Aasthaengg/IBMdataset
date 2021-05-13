import numpy as np

N, D = list(map(int, input().split()))
ans = 0
for i in range(N):
    x, y = list(map(int, input().split()))
    r2 = x**2 + y**2
    if r2 <= D**2:
        ans += 1

print(ans)