s = input()
if s == "zyxwvutsrqponmlkjihgfedcba":
  print(-1)
elif len(s) == 26:
  l = []
  for i in range(26)[::-1]:
    ds = s[i]
    l.append(ds)
    if ds != max(l):
      l.sort()
      for j in l:
        if ds < j:
          break
      print(s[:i]+j)
      break
else:
  for i in list("abcdefghijklmnopqrstuvwxyz"):
    if i in s:
      continue
    else:
      print(s+i)
      break