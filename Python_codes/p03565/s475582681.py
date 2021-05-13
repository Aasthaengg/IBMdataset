s=input()
t=input()
a=[]
ans=[]
for i in range(len(s)-len(t)+1):
  flg=0
  for j in range(len(t)):
    if s[i+j]!=t[j] and s[i+j]!='?':
      flg=1
  if flg==0:
    a.append(i)
for i in a:
  tmp=s[:i]+t+s[i+len(t):]
  for j in range(len(tmp)):
    if tmp[j]=='?':
      tmp=tmp[:j]+'a'+tmp[j+1:]
  ans.append(tmp)
ans.sort()
if ans==[]:
  print('UNRESTORABLE')
else:
  print(ans[0])