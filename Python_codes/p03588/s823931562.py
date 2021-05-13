# coding: utf-8
# Your code here!
n=int(input())
a=[0]*n
b=[0]*n
ca=0
ans=0
for i in range(n):
    a[i],b[i]=map(int,input().split())
for j in range(n):
    if a[j]>ca:
        ca=a[j]
        ans=a[j]+b[j]
print(ans)