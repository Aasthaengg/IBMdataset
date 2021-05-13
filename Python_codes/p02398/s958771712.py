nums = list(map(int, input().split()))
a = nums[0]
b = nums[1]
c = nums[2]

count = 0
for x in range(a, b + 1):
    r = c % x
    # print("%d ?? %d ... %d"%(c, x, r))
    if r == 0:
        count += 1

print(str(count))