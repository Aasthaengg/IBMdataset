s = input()
t = input()
ls = len(s)
lt = len(t)
a = []
for i in range(ls-lt+1):
  if s[i] == '?' or s[i] == t[0]:
    exists = True
    for j in range(1, lt):
      if s[i+j] != '?' and s[i+j] != t[j]:
        exists = False
        break
    if exists:
      a.append((s[:i]+t+s[i+lt:]).replace('?','a'))
if len(a) == 0:
  print("UNRESTORABLE")
else:
  print(min(a))