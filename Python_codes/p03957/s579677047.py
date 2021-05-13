s=input()
c=-1
f=-1
for i in range(len(s)):
  if s[i]=='C':
    if c==-1:
      c=i
  if s[i]=='F':
    f=max(f,i)
if c!=-1 and f>c:
  print('Yes')
else:
  print('No')