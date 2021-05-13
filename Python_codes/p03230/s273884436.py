import sys
input=lambda: sys.stdin.readline().rstrip()
from collections import defaultdict
n=int(input())
D=defaultdict(int)
i=1
while i*(i+1)//2<=10**5:
  D[i*(i+1)//2]=i
  i+=1
if D[n]==0:
  print("No")
else:
  print("Yes")
  k=D[n]+1
  print(k)
  A=[[0]*(k) for _ in range(k)]
  for i in range(k):
    A[i][0]=k-1
  D=dict()
  D[1]=1*k+1
  for i in range(2,n+1):
    d1,d2=D[i-1]//k,D[i-1]%k
    if d2==k-d1:
      D[i]=(d1+1)*k+1
    else:
      D[i]=d1*k+d2+1
  for i in range(1,n+1):
    d1,d2=D[i]//k,D[i]%k
    A[d1-1][d1+d2-1]=i
    A[d1+d2-1][d1]=i
  for a in A:
    print(*a)
