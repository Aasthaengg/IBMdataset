n,m = map(int, input().split())
ls = []
rs = []
for _ in range(m):
  l,r = map(int, input().split())
  ls.append(l)
  rs.append(r)
  
ans = min(rs) - max(ls) + 1

if ans > 0: print(ans)
else: print(0)