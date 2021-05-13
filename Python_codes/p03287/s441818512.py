import numpy as np
n, m = map(int, input().split())
a = list(map(int, input().split()))
box = {0:0}
A = 0
for i in range(n):
    A = (A+a[i]%m)%m
    if A in box:
        box[A] += 1
    else:    
        box[A] = 1

result = box[0]
for i, j in box.items():
    result += (j*(j-1))//2
print(result)