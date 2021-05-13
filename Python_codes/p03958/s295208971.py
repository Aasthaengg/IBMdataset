n,k=map(int,input().split())
l=list(map(int,input().split()))
x=max(l)
if (n+1)//2+1>x:
  print(0)
else:
  print(x-1-(sum(l)-x))