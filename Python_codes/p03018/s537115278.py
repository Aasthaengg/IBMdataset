s=input()
n=len(s)
i=0
cnt=0
ans=0
while i<n:
  if s[i]=='A':
    i+=1
    cnt+=1
    while s[i:i+2]=='BC':
      ans+=cnt
      i+=2
  else:
    cnt=0
    i+=1
print(ans)