from bisect import bisect
s=input()
n=len(s)
ls=[0]*26
if s == "zyxwvutsrqponmlkjihgfedcba":
  print(-1)
  exit()
if n<26:
  for i in range(n):
    ls[ord(s[i])-97]=i+1
  for i in range(26):
    if ls[i]==0:
      x=i
      break
  print(s+chr(x+97))
else:
  for i in range(n):
    ls[i] = ord(s[i])-97
  if ls[25]>ls[24]:
    print(s[:24]+s[25])
  else:
    tmp = []
    for i in range(24,-1,-1):
      tmp.append(ls[i+1])
      if ls[i+1]>ls[i]:
        tmps = sorted(tmp)
        x = bisect(tmps,ls[i])
        print(s[:i]+chr(tmps[x]+97))
        break