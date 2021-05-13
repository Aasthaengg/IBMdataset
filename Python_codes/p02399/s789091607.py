nums = list(map(int, input().split()))
a = nums[0]
b = nums[1]

d = a / b
r = a % b
f = float(a) / b

print("%d %d %f" % (d, r, f))