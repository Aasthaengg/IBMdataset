import re
n=int(input())
ans=0
a,b,ba=0,0,0
for i in range(n):
  s=input()
  ans+=len(re.sub("[A-Z]+","",s.replace("AB","s")))
  if s[0]=="B" and s[-1]=="A":ba+=1
  elif s[0]=="B":b+=1
  elif s[-1]=="A":a+=1
ans+=max(ba-1,0)
if ba:
  if a:ans+=1;a-=1
  if b:ans+=1;b-=1
print(ans+min(a,b))