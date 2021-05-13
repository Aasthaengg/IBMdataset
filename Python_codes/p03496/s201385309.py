import numpy as np

N = int(input())
A = np.array([0] + [int(x) for x in input().split()])

A_abs = np.abs(A)

x = A_abs.argmax()
if x == 0:
  x = 1
value = A[x]

answer = []

for j in range(1,N+1):
  if j == x:
    continue
  answer.append((x,j))
# 符号がそろった

if value > 0:
  for j in range(1,N):
    answer.append((j,j+1))
else:
  for j in range(N,1,-1):
    answer.append((j,j-1))
    
print(len(answer))
for a,b in answer:
  print(a,b)
