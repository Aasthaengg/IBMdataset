s=input()
a=set(list(s))
for i in range(26):
  if chr(ord("a")+i) not in a:
    print(s+chr(ord("a")+i))
    exit()
ans=s
for i in range(26):
  for m in s[i+1:]:
    if ord(s[i])<ord(m):
      ans=s[:i]+m
if ans==s:
  print(-1)
else:
  print(ans)