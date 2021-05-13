s=list(input())
s.sort()
t=list(input())
t.sort(reverse=True)
s=''.join(s)
t=''.join(t)
l=[s,t]
l.sort()
ans='No'
if l[0]==s and s!=t:
  ans='Yes'
print(ans)