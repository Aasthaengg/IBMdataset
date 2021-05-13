n, x, y = map(int, input().split())

dic = {}
for i in range(1, n):
  for j in range(i + 1, n + 1):
    a = j - i
    b = abs(x - i) + 1 + abs(j - y)
    c = abs(y - i) + 1 + abs(j - x)
    l = min(a, b, c)
    if l not in dic.keys():
      dic[l] = 1
    else:
      dic[l] += 1
for i in range(1, n):
  print(dic.get(i, 0))