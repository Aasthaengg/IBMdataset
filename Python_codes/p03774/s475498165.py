n,m = map(int, input().split())
ab = []
for _ in range(n):
  a,b = map(int, input().split())
  ab.append((a,b))
cd = []
for _ in range(m):
  c,d = map(int, input().split())
  cd.append((c,d))
  
for i in ab:
  s = float("inf")
  for j in range(m):
    t = abs(i[0]-cd[j][0]) + abs(i[1]-cd[j][1])
    if t < s:
      s = t
      ans = j+1
  print(ans)