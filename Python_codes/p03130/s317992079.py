from collections import Counter
lst = []
for i in range(3):
  a, b = map(int, input().split())
  lst.append(a)
  lst.append(b)
if sorted(list(Counter(lst).values())) == [1, 1, 2, 2]:
  print('YES')
else:
  print('NO')