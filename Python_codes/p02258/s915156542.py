n = int(input())
nums = [int(input()) for i in range(n)]
temp = nums[1] - nums[0]
p = nums[0]

for i in nums[1:]:
    if i - p > temp:
        temp = i- p
    if i < p:
        p = i
print(temp)