n, m = map(int, input().split())
 
a = []
 
for i in range(m):
  a1, a2 = map(int, input().split())
  a.append(a1)
  a.append(a2)
 
for s in range(n):
  print(a.count(s+1))
