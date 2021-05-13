i = [input() for i in range(2)]
a = [i for i in i[0]]
b = [i for i in i[1]]
c = 0
for i in range(3):
  if a[i] == b[i]:
    c += 1
  else:
    c += 0
print(c)