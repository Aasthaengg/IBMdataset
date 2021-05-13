N,M,C=map(int,input().split())
B=map(int,input().split())
b=list(B)
X=0
Y=C
Z=0
def mul(x,y):
  return(x*y)

for i in range(N):
  A=map(int,input().split())
  a=list(A)
  for j in range(M):
    Y=Y+a[j]*b[j]
  if Y<=0:
    Y=C
  else:
    Z=Z+1
    Y=C

print(Z)