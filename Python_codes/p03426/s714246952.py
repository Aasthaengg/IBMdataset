import sys
input=sys.stdin.readline
H,W,D = map(int,input().split())
A = []
for h in range(H):
  A = A + list(map(int,input().split()))
for i in range(H*W):
  A[i]=(A[i], i%W, i//W)
A.sort()
Dist=[0]*(H*W)
for i in range(H*W):
  if i>=D:
    Dist[i] = Dist[i-D] + abs(A[i][1]-A[i-D][1]) + abs(A[i][2]-A[i-D][2])
Q = int(input())
for q in range(Q):
  L,R = map(int,input().split())
  ret = Dist[R-1]-Dist[L-1]
  print(ret)