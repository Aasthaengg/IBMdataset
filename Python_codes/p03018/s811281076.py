s=input()
s=s.replace('BC','D')
a=0
ans=0
for i in s:
  if i=='A':
    a+=1
  elif i=='D':
    ans+=a
  else:
    a=0
print(ans)