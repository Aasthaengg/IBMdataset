n,m = map(int, input().split())
l = []
r = []
for _ in range(m):
  a,b = map(int, input().split())
  l.append(a)
  r.append(b)
  
ans = min(r) - max(l)+1
if ans > 0: print(ans)
else: print(0)