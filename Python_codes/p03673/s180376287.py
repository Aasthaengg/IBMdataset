from collections import deque
N=int(input())
L=list(input().split())
R=deque()
for i in range(N):
  if i%2==0:
    R.appendleft(L[i])
  else:
    R.append(L[i])
if N%2==0:
  R=reversed(R)
R=list(R)
print(" ".join(R))