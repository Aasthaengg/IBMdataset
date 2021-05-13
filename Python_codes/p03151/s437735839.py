N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
pD=[]
mD=[]
for i in range(N):
  d=A[i]-B[i]
  if d>=0:
    pD.append(d)
  else:
    d*=(-1)
    mD.append(d)
if sum(A)<sum(B):
  print(-1)
  exit()
if len(mD)==0:
  print(0)
  exit()
pD=sorted(pD)[::-1]
a=sum(mD)
import numpy
X=numpy.cumsum(pD)
x=0
for i in range(len(pD)):
  if X[i]>=a:
    x=(i+1)
    print(len(mD)+x)
    exit()