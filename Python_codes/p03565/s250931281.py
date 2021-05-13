s=input()
t=input()
ans=[]
for i in range(len(s)-len(t)+1):
  start=i
  end=i+len(t)
  ok=True
  for j in range(len(t)):
    if s[start+j]!='?' and s[start+j]!=t[j]:
      ok=False
      break
  if ok:
    a=s[:start]+t+s[end:]
    ans.append(a.replace('?','a'))
if ans:
  ans=sorted(ans)
  print(ans[0])
else:
  print('UNRESTORABLE')
