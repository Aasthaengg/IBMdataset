n,a,b,c,d=map(int,input().split())
s=list(input())
ch=0
ch1=0

if d<c:
  for i in range(a,c):
    if s[i]=='#':
      if s[i-1]=='#':
        ch+=1
  for j in range(b,d):
    if s[j]=='#':
      if s[j-1]=='#':
        ch+=1
  for k in range(b-1,d):
    
    if s[k-1]=='.' and s[k]=='.' and s[k+1]=='.':
      ch1+=1
      
  if ch==0 and ch1>0:
    print('Yes')
  else:
    print('No')
    
else:
  for i in range(a,c):
    if s[i]=='#':
      if s[i-1]=='#':
        ch+=1
  for j in range(b,d):
    if s[j]=='#':
      if s[j-1]=='#':
        ch+=1
  if ch==0:
    print('Yes')
  else:
    print('No')