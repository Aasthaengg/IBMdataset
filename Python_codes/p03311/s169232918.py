from statistics import median
import math
n = int(input())
a = list(map(int,input().split()))
for i in range(0,n):
    a[i] = a[i]-(i+1)
b1 = round(median(a)) 
a1 = []
a2 = []
for i in range(0,n):
    a1.append(abs(a[i]-b1))
print(sum(a1))