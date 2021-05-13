import sys
s=input()
cnt=0
for x in s:
  cnt+=1
  if x in ['U','D']:
    continue
  elif cnt %2 and x =='R':
    continue
  elif cnt%2==0 and x=='L':
    continue
  else:
    print('No')
    sys.exit()
print('Yes')