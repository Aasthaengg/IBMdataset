import numpy as np

H,W,A,B = (int(x) for x in input().split())
mt = np.zeros((H,W))
for j in range(B):
  for i in range(A):
    print(0, end="")
  for i in range(W-A):
    print(1, end="")
  print()
for j in range(H-B):
  for i in range(A):
    print(1, end="")
  for i in range(W-A):
    print(0, end="")
  print()
