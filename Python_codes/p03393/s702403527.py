s=input()
t="abcdefghijklmnopqrstuvwxyz"
if s==t[::-1]:
  print(-1)
  exit(0)
if len(s)<26:
  for ti in t:
    if not ti in s:
      print(s+ti)
      exit(0)
else:
  for i in range(25):
    if s[-i-2]<s[-1-i]:
      t=s[:-i-2]
      u=sorted(list(s[-i-2:]))
      print(t+u[u.index(s[-2-i])+1])
      exit(0)
