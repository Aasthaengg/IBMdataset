from math import ceil
n=int(input())
x=[int(input()) for i in range(5)]

bottle_neck=10**15+10

for i in range(5):
    if bottle_neck>x[i]:
        bottle_neck=x[i]

ans=ceil(n/bottle_neck)+4
print(ans)