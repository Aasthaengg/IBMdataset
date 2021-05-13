n,k = map(int, input().split())

d = {}
for _ in range(n):
  a,b = map(int, input().split())
  if a in d: d[a] += b
  else: d[a] = b
    
for x,y in sorted(d.items(), key=lambda x: x[0]):
  k -= y
  if k <= 0:
    print(x)
    exit()