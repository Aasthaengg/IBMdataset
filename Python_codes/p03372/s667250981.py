# D - Static Sushi

import sys
import numpy as np

N, C = map(int, sys.stdin.buffer.readline().split())
x, v = [], []
for _ in range(N):
    tmp, tmp2 = map(int, sys.stdin.buffer.readline().split())
    x.append(tmp)
    v.append(tmp2)

x = np.array(x, np.int64)
v = np.array(v, np.int64)
v_cum = v.cumsum()
tx = np.flipud(x)
tv_cum = np.flipud(v).cumsum()
left_cum = v_cum - x

right_cum = tv_cum - np.flipud(C - x)
right_cum_max = np.maximum.accumulate(right_cum)

right_cum_return = right_cum - np.flipud(C - x)
right_cum_return_max = np.maximum.accumulate(right_cum_return)

ans = max(0, np.max(left_cum), np.max(right_cum))

for first_abandon_idx in range(1, N):
    ans = max(ans, left_cum[first_abandon_idx-1] - x[first_abandon_idx-1] + right_cum_max[N-1 - first_abandon_idx])
    ans = max(ans, left_cum[first_abandon_idx-1] + right_cum_return_max[N-1 - first_abandon_idx])

print(ans)