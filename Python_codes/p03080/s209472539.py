n=int(input())
s=input()
ans=0
for i in s:
  if i=="R":
    ans+=1
  else:
    ans-=1
if ans>0:
  print("Yes")
else:
  print("No")