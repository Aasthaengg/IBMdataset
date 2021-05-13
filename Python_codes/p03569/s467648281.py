s=input()
i=0;j=len(s)-1
ans=0
while i<j:
  if s[i]==s[j]:
    i+=1
    j-=1
  elif s[i]=='x':
    ans+=1
    i+=1
  elif s[j]=='x':
    ans+=1
    j-=1
  else:
    print(-1)
    exit()
print(ans)