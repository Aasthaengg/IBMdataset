from math import ceil
n = int(input())
d,x = map(int,input().split())
a = list(int(input()) for i in range(n))
for i in range(n):
    x += ceil(d / a[i])
print(x)