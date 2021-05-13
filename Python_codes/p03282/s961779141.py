s=list(input())
k=int(input())
x=0
ans=0
while x<len(s) and s[x]=="1":
  x+=1
if x>0:
  if k<=x:
    ans=1
  else:
    ans=s[x]
else:
  ans=s[0]

print(ans)