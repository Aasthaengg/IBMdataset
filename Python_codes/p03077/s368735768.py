from math import ceil
n=int(input())
a=[int(input()) for i in range(5)]
x=ceil(n/(min(a)))
print(x+4)