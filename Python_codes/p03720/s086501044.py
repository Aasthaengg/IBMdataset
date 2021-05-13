n, m = map(int, input().split())
a = []
b = []
for i in range(m):
  a_, b_ = map(int, input().split())
  a.append(a_)
  b.append(b_)

for i in range(1, n+1):
  c = a.count(i)
  d = b.count(i)
  print(c+d)