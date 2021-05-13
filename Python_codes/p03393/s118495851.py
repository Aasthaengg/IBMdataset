s = input()
k = 'abcdefghijklmnopqrstuvwxyz'
if len(s) < 26:
  for v in k:
    if not v in s:
      print(s+v)
      exit()
if s == k[::-1]:
  print(-1)
  exit()
for i in range(1,len(s)+1):
  t = s[-i:]
  if t != ''.join(sorted(t, reverse=True)):
    t = t[1:]
    break
for p in t[::-1]:
  if p > s[-i]:
    print(s[:-i]+p)
    exit()