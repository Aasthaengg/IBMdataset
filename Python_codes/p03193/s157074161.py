def i(): return map(int, input().split())
n, h, w = i()
c = 0
for _ in range(n):
  a, b = i()
  c += (a >= h)*(b >= w)
print(c)