# coding: utf-8
import math
n = int(input())
#x, y = map(int,input().split())
A = list(map(int,input().split()))
ans = 0
B=  []
for i in range(n):
    B.append(A[i]-(i+1))
B.sort()
if n==1:
    m=B[0]
    m2=B[0]
else:
    m = B[n//2]
    m2=B[n//2+1]
tmp1=0
tmp2=0
#print(m,m2)
for i in range(n):
    tmp1 += abs(A[i]-(i+1)-m)
    tmp2 += abs(A[i]-(i+1)-m2)
print(min(tmp1, tmp2))