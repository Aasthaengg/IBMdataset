# https://atcoder.jp/contests/abc067/tasks/arc078_a

n = int(input())
nums = [int(i) for i in input().split()]

for i in range(n - 1):
    nums[i + 1] += nums[i]

ans = float('inf')
for i in range(n - 1):
    x = nums[i]
    y = nums[-1] - nums[i]
    ans = min(ans, abs(x - y))
print(ans)
