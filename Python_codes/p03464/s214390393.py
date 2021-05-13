import math
k = int(input())
a = [int(item) for item in input().split()]
a.reverse()

max_num = 2 
min_num = 2 
for i in range(k):
    if int(math.floor(max_num / a[i])) * a[i] < int(math.ceil(min_num / a[i])) * a[i]:
        print(-1)
        exit()
    next_max = int(math.floor(max_num / a[i])) * a[i] + a[i] - 1
    next_min = int(math.ceil(min_num / a[i])) * a[i]
    max_num = next_max
    min_num = next_min
print(min_num, max_num)