s=input()
g,p,ans=0,0,0
for i in range(len(s)):
  if s[i]=="p":
    if g==p:
      g+=1
      ans-=1
    else:
      p+=1
  elif g==p:
    g+=1
  else:
    p+=1
    ans+=1
print(ans)