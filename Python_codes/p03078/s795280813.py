import sys
input = sys.stdin.readline

x, y, z, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]
a.sort()
b.sort()
c.sort()

x_y_list = []

for i in a:
    for j in b:
        x_y_list.append(i + j)

x_y_list.sort()

import bisect
left = 0
right = 10 ** 18

import numpy as np

x_y_list_np = np.array(x_y_list, np.int64)
c_np = np.array(c, np.int64)

while right - left > 1:
    mid = (left + right) // 2
    cnt = np.searchsorted(x_y_list_np, mid - c_np, side="right").sum()
    if cnt >= x*y*z - k + 1:
        right = mid
    else:
        left = mid

up_k = right # 上からk番目

ans = []
for i in c:
    idx = bisect.bisect_right(x_y_list, up_k - i)
    for j in range(idx, len(x_y_list)):
        ans.append(i + x_y_list[j])

for i in range(k - len(ans)):
    ans.append(up_k)

ans.sort()

for i in ans[::-1]:
    print(i)