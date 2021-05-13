s=input() 
ans=0
for i in range(0,len(s),2):
  if s[i]!='R' and s[i]!='U'  and s[i]!='D':
    ans=1
for j in range(1,len(s),2):
  if s[j]!='U' and s[j]!='L' and s[j]!='D':
    ans=1
if ans==0:
  print('Yes')
else:
  print('No')
