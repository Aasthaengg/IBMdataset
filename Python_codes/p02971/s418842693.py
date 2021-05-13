import math
N = int(input())
A = [0]*N
B = [0]*N
for i in range(N):
  A[i]= int(input())
B = sorted(A,reverse=True)
for j in range(N):
  if(A[j]==B[0]):
    print(B[1])
  else:
    print(B[0])
