n = int(input())
a = [int(x) for x in input().split()]
a.sort(reverse=True)
key = []
p = -1
for i in range(1, n):
  if p == i:
    continue
  if a[i] == a[i-1]:
    key.append(a[i])
    if len(key) == 2:
      break
    p = i+1
if len(key) < 2:
  print(0)
else:
  print(key[0]*key[1])