import sys
stdin=sys.stdin

ip=lambda: int(sp())
fp=lambda: float(sp())
lp=lambda:list(map(int,stdin.readline().split()))
sp=lambda:stdin.readline().rstrip()

n=ip()
a=[]
b=[]
ans=0
for i in range(n):
  s=sp()
  if s[0]=='B':
    b.append(i)
  if s[-1]=='A':
    a.append(i)
  for j in range(len(s)-1):
    if s[j]=='A' and s[j+1]=='B':
      ans+=1
      
c=len(list(set(a)&set(b)))
a_rest=len(a)-c
b_rest=len(b)-c
if c==0:
  omake=min(a_rest,b_rest)
else:
  if a_rest==b_rest==0:
    omake=c-1
  else:
    omake=c+min(a_rest,b_rest)
  
print(ans+omake)


