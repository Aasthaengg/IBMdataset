# ABC138
# B Resistors in Parallel
import math
n = int(input())
A = list(map(int, input().split()))
y = 0
for i in A:
    y += 1000/i
x = 1/y*1000
print(x)
