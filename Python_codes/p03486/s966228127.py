s=[x for x in input()]
t=[x for x in input()]
s=sorted(s)
t=sorted(t,reverse=True)
s=''.join(s)
t=''.join(t)

ans=[]
ans.append(s)
ans.append(t)
ans.sort()

if s==t:
  print('No')
elif ans[0]==s:
  print('Yes')
else:
  print('No')