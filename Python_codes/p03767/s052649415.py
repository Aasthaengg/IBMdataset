# https://atcoder.jp/contests/agc012/tasks/agc012_a

n = int(input())
nums = [int(i) for i in input().split()]
nums.sort()
nums = nums[n:]

ans = 0
for i in range(0, len(nums), 2):
    ans += nums[i]
print(ans)