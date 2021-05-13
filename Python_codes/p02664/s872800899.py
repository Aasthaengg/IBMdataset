S = input()
s=[]
for i in S:
    s.append(i)
t = []
for i in range(len(s)):
  if s[i] == '?':
    t.append('D')
  else:
    t.append(s[i])
Strt = "".join(t)
print(Strt)