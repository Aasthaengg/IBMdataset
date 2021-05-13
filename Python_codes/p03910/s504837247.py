N = int(input())
total = 0
res = []

for i in range(5000)[1:]:
  res.append(i)
  total += i
  if N <= total:
    break
if total != N:
  res.remove(total - N)
for r in res:
  print(r)