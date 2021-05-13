import numpy as np
A = np.array([list(map(int,input().split())) for n in range(3)])
N = int(input())
B = [int(input()) for i in range(N)]

for b in B:
  A = np.where(A==b,0,A)

if np.any(np.all(A==0,axis=0)) or np.any(np.all(A==0,axis=1)):
  print("Yes")
  
elif A[0][0]==A[1][1]==A[2][2]==0 or A[0][2]==A[1][1]==A[2][0]==0:
  print("Yes")
  
else:
  print("No")