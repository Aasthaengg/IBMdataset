n = int(input())
c = 0
isthere = 0
for i in range(n):
    nums = [int(prefix_sum) for prefix_sum in input().split()]
    if nums[0] == nums[1]:
        c = c + 1
    else:
        c = 0

    if c >= 3:
        isthere = 1

if isthere == 1:
    print('Yes')
else:
    print('No')
