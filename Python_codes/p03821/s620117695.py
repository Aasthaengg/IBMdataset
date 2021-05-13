# coding: utf-8
import math
n=int(input())
A=[]
B=[]
for i in range(n):
    a, b = map(int,input().split())
    A.append(a)
    B.append(b)
cnt=0
for i in range(n-1,-1,-1):
    a=A[i]
    b=B[i]
    cnt += math.ceil((a+cnt)/b)*b-(a+cnt)
print(cnt)