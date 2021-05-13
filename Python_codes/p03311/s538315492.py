# https://atcoder.jp/contests/arc100/tasks/arc100_a

n = int(input())
nums = [int(i) for i in input().split()]

for i in range(n):
    nums[i] -= i + 1
nums.sort()
ans = 0
mid = nums[n // 2]
for i in range(n):
    ans += abs(nums[i] - mid)
print(ans)