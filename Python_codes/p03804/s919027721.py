import numpy as np

N,M=map(int,input().split())
A=np.array([list(input()) for _ in range(N)])
B=np.array([list(input()) for _ in range(M)])

bl=False
for i in range(N-M+1):
  for j in range(N-M+1):
    if (A[i:i+M,j:j+M]==B).all():
      bl=True

answer='Yes' if bl else 'No'
print(answer)