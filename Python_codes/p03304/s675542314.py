
nums = list(map(int, input().split()))
n = nums[0]
m = nums[1]
d = nums[2]
if d == 0:
    print((m - 1) / n)
else:
    print((m - 1) / n * 2 * (n - d) / n)
