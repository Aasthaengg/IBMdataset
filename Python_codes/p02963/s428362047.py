S = int(input())
from math import sqrt, ceil
rtS = sqrt(S)
u = 10 ** 9
ans = [0 for _ in range(6)]
ans[2] = u
ans[3] = 1
ans[5] = ceil(S/u)
ans[4] = ans[5] * u - S
print(*ans)