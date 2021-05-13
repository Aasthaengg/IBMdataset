N,K = map(int,input().split())
S = list(input())

# nums[i]: iが偶数なら1の個数 奇数なら0の個数
nums = []

if S[0] == "0":
    nums.append(0)

# 尺取り法
left = 0
while left < N:
    right = left
    while right < N and S[right] == S[left]:
        right += 1
    nums.append(right - left)
    left = right

if S[-1] == "0":
    nums.append(0)

from itertools import accumulate

nums = [0] + list(accumulate(nums))

ans = 0
for left in range(0, len(nums), 2):
    right = min(len(nums) - 1, left + 2 * K + 1)
    ans = max(ans, nums[right] - nums[left])

print(ans)