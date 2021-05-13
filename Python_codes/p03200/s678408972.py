a = input()
b = int(len(a))
c = int(0)
d = int(0)
e = int(0)
for i in range(b):
  if a[i] == "W":
    c += 1

for i in range(b):
  if a[i] == "W":
    e = e + int(i) - d
    d += 1

print(e)
