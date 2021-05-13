N = int(input())
nums = [int(i) for i in input().split()]


nums = sorted(nums, reverse=True)


a_sum = 0
for i in range(1,N):
    index = i//2
    a_sum += nums[index]

print(a_sum)