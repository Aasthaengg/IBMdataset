N=int(input())
A=[list(map(int,input().split())) for i in range(N)]
a=A[0][0]
b=A[0][1]
import fractions
for i in range(1,N):
  if a<=A[i][0] and b<=A[i][1]:
    a=A[i][0] 
    b=A[i][1]
  else:
    aa=1
    bb=1
    if a>A[i][0]:
      if a%A[i][0]==0:
        aa=a//A[i][0]
      else:
        aa=1+a//A[i][0]
    if b>A[i][1]:
      if b%A[i][1]==0:
        bb=b//A[i][1]
      else:
        bb=1+b//A[i][1]
    c=max(aa,bb)
    a=c*A[i][0]
    b=c*A[i][1]
print(a+b)