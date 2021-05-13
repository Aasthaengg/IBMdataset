n, d = map(int, input().split())
p = []
for _ in range(n):
  p.append(list(map(int, input().split())))
d2 = d*d
a = 0
for i in range(n):
  if(p[i][0]**2+p[i][1]**2 <= d2):
    a += 1
print(a)