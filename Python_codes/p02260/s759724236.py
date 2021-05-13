n = int(input())
nums = list(map(int, input().split()))
count = 0

for i in range(n):
    minj = i

    for j in range(i + 1, n):
#    for j in range(i, n):
        if nums[j] < nums[minj]:
            minj = j
#            count += 1
    else:
        if nums[i] > nums[minj]:
            temp = nums[minj]
            nums[minj] = nums[i]
            nums[i] = temp
            count += 1

print(' '.join([str(i) for i in nums]))
print(count)

