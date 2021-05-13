
nums1 = []
sum = 0
for i in range(2):
    nums = [int(e) for e in input().split()]
    nums1.append(nums)

max = nums1[1][0]
min = nums1[1][0]
sum = 0

for i in range(len(nums1[1])):
    if nums1[1][i]>max:
        max = nums1[1][i]
    if nums1[1][i]<min:
        min = nums1[1][i]
    sum = sum + nums1[1][i]
    
print(min, max, sum)
