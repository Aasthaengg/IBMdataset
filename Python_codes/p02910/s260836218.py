s=list(input())
ch=0
for i in range(len(s)):
  if (i+1)%2==0:
    if s[i]=='R':
      ch+=1
  else:
    if s[i]=='L':
      ch+=1
      
if ch==0:
  print('Yes')
else:
  print('No')