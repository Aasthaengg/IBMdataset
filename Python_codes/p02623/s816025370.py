import numpy as np
from bisect import bisect_right

n, m, k = map(int, input().split())
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))
a = np.cumsum(a)
b = np.cumsum(b)

ans = 0
for a_num, time in enumerate(a):
    if time > k:
        continue
    b_num = bisect_right(b, k - time)
    num = a_num + b_num - 1
    if num > ans:
        ans = num
print(ans)
