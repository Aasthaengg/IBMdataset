n1 = int(raw_input())
nums1 = map(int, raw_input().split(" "))
n2 = int(raw_input())
nums2 = map(int, raw_input().split(" "))
nums1.append(-1)
count = 0

for key in nums2:
    nums1[len(nums1)-1] = key
    idx = 0

    while nums1[idx] != key:
        idx += 1

    if idx != len(nums1)-1:
        count += 1

print(count)