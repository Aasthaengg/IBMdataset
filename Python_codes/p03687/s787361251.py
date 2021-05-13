s=input()
ans=10**5
for a in set(list(s)):
  t=s
  for i in range(len(s)):
    u=''
    for j in range(len(t)-1):
      if t[j+1]==a or t[j]==a:
        u+=a
      else:
        u+=t[j+1]
    t=u
    if len(set(list(u)))==1:
      ans=min(ans,i+1)
      break
if len(set(list(s)))==1:
  ans=0
print(ans)