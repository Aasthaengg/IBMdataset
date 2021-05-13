s = input()
t = input()
d = {}
d2 = {}
for i in range(len(s)):
  if t[i] in d:
    if d[t[i]] != s[i]:
      print("No")
      break
  if s[i] in d2:
    if d2[s[i]] != t[i]:
      print("No")
      break
  else:
    d[t[i]] = s[i]
    d2[s[i]] = t[i]
else:
  print("Yes")
