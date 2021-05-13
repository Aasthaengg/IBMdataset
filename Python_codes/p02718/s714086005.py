n,m=map(int,input().split())
l=list(map(int,input().split()))
wa=0
for i in range(n):
  wa+=l[i]
ans=0
for i in range(n):
  if l[i]>=wa/4/m:
    ans+=1
if ans>=m:
  print("Yes")
else:
  print("No")