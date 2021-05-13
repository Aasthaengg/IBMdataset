s=input()
ans=0
bc=0
i=len(s)-1
while i>=0:
  if s[i]=="A":
    ans+=bc
    i-=1
  elif i>0 and s[i-1:i+1]=="BC":
    bc+=1
    i-=2
  else:
    bc=0
    i-=1
print(ans)