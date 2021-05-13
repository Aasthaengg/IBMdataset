import sys
from collections import deque

def input():
  return sys.stdin.readline()

N,M=map(int,input().split())
L=[[] for _ in range(N)]
for _ in range(M):
  a,b=map(int,input().split())
  L[a-1].append(b)
  L[b-1].append(a)
A=[0]*N
a,b = N,0
d=deque([])
for l in L[0]:
  d.append((1,l))
while a>b:
  i,j=d.popleft()
  if A[j-1]==0:
    b+=1
    A[j-1]=i
    for l in L[j-1]:
      d.append((j,l))
if a==b:
  print("Yes")
  for i in range(1,N):
    print(A[i])
else:
  print("No")