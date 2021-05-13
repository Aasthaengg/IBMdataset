s = input()
t = input()
u = 0

if s == t:
  print(0)
else:
  for i in range(len(s)):
    if s[i] != t[i]:
      u += 1
  print(u)
