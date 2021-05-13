vals = []
for line in range(3):
  s = input().split()
  val = []
  for v in s:
    val.append(int(v))
  vals.append(val)

info = True

a = [0,]
b = vals[0]
a.append(vals[1][0]-b[0])
a.append(vals[2][0]-b[0])

for i in range(3):
  for j in range(3):
    if vals[i][j] != a[i] + b[j]:
      info = False
print('Yes' if info else 'No')