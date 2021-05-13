n,m = map(int,input().split())
s = []
for i in range(n):
  s.append(tuple(map(int,input().split())))
p = []
for i in range(m):
  p.append(tuple(map(int,input().split())))

for a,b in s:
  mnl = float('inf')
  for i in range(m):
    c,d = p[i]
    l = abs(a-c)+abs(b-d)
    if l < mnl:
      mnp = i+1
      mnl = l
  print(mnp)
