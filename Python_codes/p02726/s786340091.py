import math
nums = [int(i) for i in input().split()]
n = nums[0]
x = nums[1]
y = nums[2]
res = [0 for i in range(2010)]

for i in range(1, n+1):
    for j in range(i+1, n+1):
        dis = j - i
        dis = min(dis, abs(i-x)+abs(j-y)+1)
        res[dis] += 1
for i in range(1, n):
    print(res[i])
