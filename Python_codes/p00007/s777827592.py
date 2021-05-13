from math import ceil
n = int(input())

a = 100
for i in range(n):
    a=ceil(1.05 * a)
print (a*1000)