N=int(input())
A,B=map(int,input().split())
P=list(map(int,input().split()))
x=0
y=0
z=0
for p in P:
  if p<=A:
    x+=1
  elif A+1<=p and p<=B:
    y+=1
  else:
    z+=1
print(min(x,y,z))    