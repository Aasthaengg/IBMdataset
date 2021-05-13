ab = []
for i in range(3):
  p, q = map(int, input().split())
  ab.append(p)
  ab.append(q)
o, d = 0, 0
count = 0
for i in range(1, 5):
  if ab.count(i) == 2 or ab.count(i) == 1:
    count += 1
if count == 4:
  print('YES')
else:
  print('NO')