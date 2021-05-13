import math
N = int(input())
T = [int(input()) for _ in range(5)]

ans = 0
m = N
for i, t in enumerate(T):
    if m > t:
        m = t
        ans = math.ceil(N/m) + i
    else:
        ans += 1
print(ans)
