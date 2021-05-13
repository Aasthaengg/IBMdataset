import math
n, l = map(int, input().split())
a_l = [l + i for i in range(n)]
 
min1 = 100
min2 = 10000
 
for j in a_l:
    if j ** 2 <= min2:
        min2 = j **2
        min1 = j
print(sum(a_l) - min1)