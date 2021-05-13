import math
from itertools import permutations 
N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
ans_ = 0
count = 0
sum_list = list(permutations(range(N), N))
for nums in sum_list:
    for i in range(len(nums)-1):
        x1, y1 = xy[nums[i]]
        x2, y2 = xy[nums[i+1]]
        ans_ += math.sqrt((x1-x2)**2+(y1-y2)**2)
    count += 1
print(ans_ / count)