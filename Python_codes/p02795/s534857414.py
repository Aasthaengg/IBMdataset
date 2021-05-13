from math import ceil
h=int(input())
w=int(input())
n=int(input())
res=ceil(n/max(h,w))
print(res)