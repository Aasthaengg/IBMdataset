s = input()
a = s[0]
c = 0
for i in range(len(s)):
  if a == s[i]:
    pass
  else:
    c += 1
    a = s[i]
print(c)