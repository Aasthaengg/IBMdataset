k = int(input())
nums = []

def rec(d, val, nums):
    nums.append(val)
    if d == 10:
        return
    for i in range(-1, 2):
        add = val%10 + i
        if (0<= add <= 9):
            rec(d+1, val*10+add, nums)
for j in range(1,10):
    rec(1,j,nums)

nums.sort()
print(nums[k-1])