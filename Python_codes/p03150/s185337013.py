s=input()
x=len(s)-7
if x==0:
  if  s=='keyence':
    print('YES')
    exit()
  else:
    print('NO')
    exit()

if s[:7]=='keyence':
    print('YES')
    exit()


for i in range(len(s)-5):
  if s[:i]+s[i+x:]=='keyence':
    print('YES')
    exit()
    
print('NO')
