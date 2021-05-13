n, l = map(int, input().split())
p = []
q = []
for i in range(n):
  p.append(abs(l + i))
  q.append(l + i)
a = 0
for i in range(n):
  if i != p.index(min(p)):
    a += q[i]
print(a)