import collections
h, w, n = map(int, input().split(" "))
list_include = []
for i in range(n):
  a, b = map(int, input().split(" "))
  for y in range(3):
    for x in range(3):
      if a - y > 0 and a - y + 2 <= h:
        if b - x > 0 and b - x + 2 <= w:
          list_include.append((a - y, b - x))
count = collections.Counter(list_include)
result = [0 for _ in range(10)]
for item in count.items():
  result[item[1]] += 1
result[0] = (h - 2) * (w - 2) - sum(result)
for one_result in result:
  print(one_result)
