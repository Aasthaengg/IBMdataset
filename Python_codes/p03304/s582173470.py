n, m, d = map(int, input().split())
c = n
if d:
  c = 2 * (n - d)
print(c * (m -1)/ n ** 2)
