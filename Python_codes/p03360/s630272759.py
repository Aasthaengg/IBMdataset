import math,numpy, collections

a = list(map(int,input().split()))
n = int(input())

for i in range(n):
    a.sort(reverse=True)
    a[0] *= 2
print(sum(a))