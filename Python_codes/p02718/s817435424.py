n,m=map(int,input().split())
a=list(map(int,input().split()))
b=sum(a)
a.sort()
ans=0
for x in a:
  if x>=(b/(4*m)):
    ans+=1

if ans>=m:
  print("Yes")
else:
  print("No")
