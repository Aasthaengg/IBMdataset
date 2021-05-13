s=input()
n=int(input())
ans=0
tmp=1
for i in range(len(s)-1):
  if s[i]==s[i+1]:
    tmp+=1
  else:
    ans+=tmp//2
    tmp=1
if tmp!=0:
  ans+=tmp//2
ans*=n
if len(s)!=1 and s[0]==s[-1]:
  top=0
  bottom=0
  for i in range(len(s)):
    if s[:i].count(s[0])==i:
      top=i
    if s[-i:].count(s[-1])==i:
      bottom=i
  if top!=len(s)-1:
    ans-=(top//2+bottom//2-(top+bottom)//2)*(n-1)
  elif len(s)%2==1:
    ans+=n//2
if len(s)==1:
  print(n//2)
else:
  print(ans)