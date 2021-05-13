def match(s,t):
  for i in range(m):
    if s[i]==t[i] or s[i]=='?':
      continue
    return False
  return True
s = list(input())
t = list(input())
n = len(s)
m = len(t)
i = n-m
found = False
while i >= 0:
  if match(s[i:i+m],t):
    found = True
    for j in range(i,i+m):
      s[j] = t[j-i]
    break
  i-=1
if found:
  for i in s:
    if i=='?':
      print('a',end='')
    else:
      print(i,end='')
  print()
else:
  print("UNRESTORABLE")