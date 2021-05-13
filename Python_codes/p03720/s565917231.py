a,b=map(int,input().split())
L=[0]*a
for i in range(b):
  x,y=map(int,input().split())
  L[x-1]+=1
  L[y-1]+=1
for i in range(a):
  print(L[i])