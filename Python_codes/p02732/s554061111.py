n = int(input())
a = list(map(int, input().split()))

nums = [0] * (max(a) + 1)
for i in range(len(a)):
    nums[a[i]] += 1

from scipy.special import comb

all = 0
for i in range(len(nums)):
    all += comb(nums[i], 2, exact=True)

for k in range(n):
    print(all - (nums[a[k]] - 1))
