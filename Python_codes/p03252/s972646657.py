s=list(input())
t=list(input())

import sys
dic_s={}
dic_t={}

for i in range(len(s)):
  a=dic_s.get(s[i],t[i])
  b=dic_t.get(t[i],s[i])
  if a!=t[i] or b!=s[i]:
    print("No")
    sys.exit()
  dic_s[s[i]]=t[i]
  dic_t[t[i]]=s[i]
print("Yes")

