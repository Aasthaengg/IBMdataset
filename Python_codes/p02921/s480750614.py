s = list(input())
t = list(input())
l = list()
for i in range(3):
  l.append(1) if s[i] == t[i] else l.append(0)
print(sum(l))