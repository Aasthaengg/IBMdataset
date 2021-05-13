s=input()
ans='AC'
if s[0]!='A':
  ans='WA'
s=s[1:]
if s[1:-1].count('C')!=1:
  ans='WA'
s=s.replace('C','c')
for i in s:
  if i.islower()==False:
    ans='WA'
    break
print(ans)
