nums = list(map(int, input().split()))
total_diff = 0
max_num = max(nums)
for i in range(3):
    total_diff += max_num - nums[i]

if total_diff % 2 == 1:
    max_num += 1

print(int((max_num * 3 - sum(nums)) / 2))
