N = int(input())
nums = list(map(int, input().split(" ")))

all_sum = sum(nums)
sums = [None] * N

min_diff_value = float('inf')
min_diff_index = -1


for i in range(N-1):
    if i==0:
        sums[i] = nums[i]
    else:
        sums[i] = sums[i-1] + nums[i]

    lhs_value = sums[i]
    rhs_value = all_sum - lhs_value
    diff_value = abs(lhs_value - rhs_value)

    if diff_value < min_diff_value:
        min_diff_value = diff_value

print(min_diff_value)        





