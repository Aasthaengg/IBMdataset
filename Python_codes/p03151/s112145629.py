import numpy as np
from bisect import bisect_right

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

diff = [0 for i in range(N)]
need = 0
ans = 0

for i in range(N):
    diff[i] = A[i] - B[i]
    if diff[i] < 0:
        need += -diff[i]
        ans += 1
        diff[i] = 0

diff = sorted(diff, reverse=True)  # 大きい順
cumsum = np.cumsum(diff)

if need != 0:
    ans += bisect_right(cumsum, need)+1
if ans > N:
    ans = -1
print(ans)
