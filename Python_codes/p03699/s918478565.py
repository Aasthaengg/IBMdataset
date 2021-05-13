import sys

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
s = sum(nums)
if s % 10 != 0:
    print(s)
else:
    nums.sort()
    for num in nums:
        t = s - num
        if t % 10 != 0:
            print(t)
            break
    else:
        print(0)