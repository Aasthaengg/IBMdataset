s = input()
l = [0]
c = 0
for i in s:
  if i in "ACGT":
    c += 1
  else:
    l.append(c)
    c = 0
l.append(c)
print(max(l))