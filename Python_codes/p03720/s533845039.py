n, m = map(int, input().split())
l = []
for i in range(m):
  l.extend(map(int, input().split()))
for i in range(n):
  print(l.count(i+1))