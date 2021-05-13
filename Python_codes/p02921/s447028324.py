a = []
for i in range(2):
    a.append(input())

c = 0
for i in range (3):
  if a[0][i] == a[1][i]:
    c += 1
print(c)