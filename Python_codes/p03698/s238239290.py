import collections
a = input()
b = []
c = int(len(str(a)))

for i in range(c):
  b.append(a[i])

d = collections.Counter(b)
e = d.most_common()[0][1]

if e != 1:
  print("no")
else:
  print("yes")