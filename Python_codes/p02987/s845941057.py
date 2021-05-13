s=list(input())
a=len(set(s))
ans='No'
if a==2:
  b=len([t for t in s if t==s[0]])
  if b==2:
    ans='Yes'
print(ans)