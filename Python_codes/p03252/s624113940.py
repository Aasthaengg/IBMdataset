import sys

s=list(str(input()))
t=list(str(input()))

start=[-1 for _ in range(26)]
goal=[-1 for _ in range(26)]

for i in range(len(s)):
  a=int(ord(s[i]))-97
  b=int(ord(t[i]))-97

  if start[a]!=-1 or goal[b]!=-1:
    if start[a]!=b or goal[b]!=a:
      print('No')
      sys.exit()
  start[a]=b
  goal[b]=a

print('Yes')