import re
s,t=input().replace(*"?."),input()
l,m,*c=len(s),len(t)
for i in range(l-m+1):
 if re.match(s[i:i+m],t):c+=(s[:i]+t+s[i+m:]).replace(*".a"),
print(c and min(c)or"UNRESTORABLE")