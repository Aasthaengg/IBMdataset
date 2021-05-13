# https://atcoder.jp/contests/agc011/tasks/agc011_b
from copy import deepcopy
n = int(input())
nums = [int(i) for i in input().split()]
nums.sort()
cums = deepcopy(nums)
for i in range(1, n):
    cums[i] += cums[i - 1]

t = 1
for i in range(n - 1)[::-1]:
    if nums[i + 1] <= cums[i] * 2:
        t += 1
    else:
        break
print(t)