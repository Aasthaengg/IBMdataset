import math

a, b, c, x = [int(input()) for _ in range(4)]

ans = 0
a_min = max(0, math.ceil((x - 100 * b - 50 * c) / 500))
a_max = min(a, math.floor(x / 500))
for ai in range(a_min, a_max + 1):
    b_min = max(0, math.ceil((x - 500 * ai - 50 * c) / 100))
    b_max = min(b, math.floor((x - 500 * ai) / 100))
    ans += b_max - b_min + 1
print(ans)
