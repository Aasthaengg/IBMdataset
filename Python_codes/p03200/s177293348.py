s=list(input())
ans=0
ch=0
for x in range(len(s)):
  if s[x]=='W':
    ans+=(x-ch)
    ch+=1
    
print(ans)

