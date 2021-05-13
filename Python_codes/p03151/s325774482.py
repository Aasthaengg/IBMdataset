import sys
N=int(input())
C=list()
A=list(map(int,input().split()))
B=list(map(int,input().split()))
R=0
k=0
if sum(B)>sum(A):
  print(-1)
  sys.exit()
for i in range(N):
  C.append(A[i]-B[i])
C=sorted(C)
for i in range(N):
  if C[i]<0:
    R=R+C[i]
    k=k+1
C=sorted(C,reverse=True)
for i in range(N):
  if R==0:
    print(0)
    sys.exit()
  R=R+C[i]
  if R>=0:
    print(k+i+1)
    sys.exit()