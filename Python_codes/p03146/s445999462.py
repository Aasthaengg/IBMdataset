a = []
a.append(int(input()))
i = 1
while True:
  x = a[-1]
  if x % 2 == 0:
    y = x // 2
    a.append(y)
  else:
    y = 3 * x + 1
    a.append(y)
  if a.count(y) >= 2:
    break
print(len(a))