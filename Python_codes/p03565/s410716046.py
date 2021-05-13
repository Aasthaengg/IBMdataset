s=input()
t=input()
n=len(s)
m=len(t)
ans='UNRESTORABLE'
a=[]
for i in range(n-m+1):
  if s[i]==t[0] or s[i]=='?':
    for j in range(m):
      if s[i+j]!=t[j] and s[i+j]!='?':
        break
    else:
      an=list(s[:i]+t+s[i+j+1:])
      for k in range(n):
        if an[k]=='?':
          an[k]='a'
      an=''.join(an)
      a.append(an)
if len(a):
  print(min(a))
else:print(ans)