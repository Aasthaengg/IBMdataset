s=input()
aflag=0
bflag=0
cflag=0
for i in range(3):
  if s[i]=='a':
    aflag+=1
  if s[i]=='b':
    bflag+=1
  if s[i]=='c':
    cflag+=1
if aflag==1 and bflag==1 and cflag==1:
  print('Yes')
else:
  print('No')