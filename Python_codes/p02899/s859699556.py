# coding: utf-8
# Your code here!

n=int(input())
l=list(map(int,input().split()))
A=[]
for i in range(n):
    A.append([l[i],i+1])
A.sort()
for i in range(n):
    print(A[i][1],end=" ")