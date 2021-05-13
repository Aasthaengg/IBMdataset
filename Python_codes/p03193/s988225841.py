import re
A = list()
B = list()
stack = 0
N,H,W = map(int,input().split())

for i in range(N):
  a,b = map(int,input().split())
  A.append(a)
  B.append(b)

for j in range(N):
  #print(A[j],B[j])
  if A[j] >= H and B[j] >= W:
    stack = stack + 1
    #print("stack!")
#print(N,H,W)
print(stack)
