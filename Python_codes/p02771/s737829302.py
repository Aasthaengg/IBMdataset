a,b,c=map(int,input().split())
l=[b,c]
ans=0
for i in l:
  if a==i:
    ans+=1
if b==c:
  ans+=1
if ans==1:
  print("Yes")
else:
  print("No")