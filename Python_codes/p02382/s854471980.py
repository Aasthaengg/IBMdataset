import math
n = int(input())
array = [[int(i) for i in input().split()] for i in range(2)] 
p1 = 0
p2 = 0
p3 = 0
pm = []
for i in range(n):
    p1 +=math.fabs(array[0][i]-array[1][i])
    p2 +=math.fabs(array[0][i]-array[1][i])**2
    p3 +=math.fabs(array[0][i]-array[1][i])**3
    pm.append(math.fabs(array[0][i]-array[1][i]))
print(p1)
print(math.sqrt(p2))
print(p3**(1/3))
print(max(pm))