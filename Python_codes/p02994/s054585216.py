A,B=map(int,input().split())
tot=A*(A+2*B-1)//2
X=B
Y=A+B-1
if abs(X)<abs(Y):
  Z=X
else:
  Z=Y
if X<=0 and Y>=0:
  print(tot)
else:
  print(tot-Z)