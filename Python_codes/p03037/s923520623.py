n,m = map(int,input().split())
l_max=1
r_min=10**5 
for i in range(m):
  l,r = map(int,input().split())
  l_max = max(l_max,l)
  r_min = min(r_min,r)
ans = r_min - l_max + 1
print(ans if ans >= 0 else 0 )