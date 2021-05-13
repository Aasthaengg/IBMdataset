n = int(input())
a = []
for i in range(1, n+1):
  c = 0
  while True:
    if i % 2 != 0:
      break
    i = i // 2
    c += 1
  a.append(c)
print(a.index(max(a)) + 1)