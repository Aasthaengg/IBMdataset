N=int(input())
A,B=map(int,input().split())
P=sorted(list(map(int,input().split())))
X=0
Y=0
Z=0
for i in range(N):
  if P[i]<=A:
    X+=1
  elif A+1<=P[i]<=B:
    Y+=1
  else:
    Z+=1
X=min(X,Y)
print(min(X,Z))