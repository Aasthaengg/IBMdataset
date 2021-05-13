s=[s for s in input()]
alp=[chr(ord('a')+i) for i in range(26)]
n=len(s)
ans=10**9
for a in alp:
  t=s
  if not a in s:continue
  for i in range(n):
    if len(set(t))==1:break
    b=[]
    for j in range(n-i-1):
      if t[j]==a:b+=[t[j]]
      elif t[j+1]==a:b+=t[j+1]
      else:b+=t[j]
    t=b
  ans=min(ans,i)
print(ans)