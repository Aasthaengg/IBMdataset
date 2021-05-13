n,a,b,c,d=map(int,input().split())
s=str(input())
s=list(s)
cnts=0
cnti=0
space=0
iwa=0
temp=0
next=0
if c<d:
  for i in range(a-1,d):
    if s[i]==".":
      cnts=cnts+1
      space=max(space,cnts)
      cnti=0
    else:
      cnti=cnti+1
      iwa=max(iwa,cnti)
      cnts=0
  if iwa>1:
    print("No")
  else:
    print("Yes")
else:
  for i in range(a-1,c):
    if s[i]==".":
      if i<=b-2:
        cnts=0
      cnts=cnts+1
      space=max(space,cnts)
      cnti=0
    else:
      cnti=cnti+1
      iwa=max(iwa,cnti)
      cnts=0
    if i==d-1:
      temp=space
      if s[i-1]=="." and s[i+1]==".":
        next=1
  if iwa>1:
    print("No")
  elif temp<3 and next==0:
    print("No")
  else:
    print("Yes")