s = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'
if len(s) < 26:
  for c in alpha:
    if c not in s:
      print(s + c)
      break
else:
  sr = {s[-1]}
  for i in range(1, len(s)):
    leng = len(s) - i - 1
    if max(sr) > s[leng]:
      print(s[:leng] + min(c for c in sr if c > s[leng]))
      break
    sr.add(s[leng])
  else:
       print(-1)