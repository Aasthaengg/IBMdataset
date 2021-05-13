s=input()

cnt=0

for i in range(0,len(s),2):
  if s[i]=='L':
    cnt+=1

for i in range(1,len(s),2):
  if s[i]=='R':
    cnt+=1

if cnt==0:
  print('Yes')
else:
  print('No')