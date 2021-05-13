a = int(input())
b = int(input())
c = int(input())
xdvd = int(input())
res = 0
for al in range(a + 1):
  for be in range(b + 1):
    for ga in range(c + 1):
      if 500 * al + 100 * be + 50 * ga == xdvd:
        res += 1
print(res)