s = input()
t = input()
o = []
for i in range(len(s)):
  if s[i] != t[i]:
    o.append(s[i])
print(len(o))