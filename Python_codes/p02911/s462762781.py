import math

n,k,q = map(int,input().split())
A=[0]*q
B=[0]*n
for i in range(q):
  A[i] = int(input())-1
for ii in range(q):
  B[A[ii]] +=1
for j in range(n):
  if(k+B[j]-q>0):
    print("Yes")
  else:
    print("No")