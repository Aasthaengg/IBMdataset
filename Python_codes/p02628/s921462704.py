n, k = map(int,input().split())
p = list(map(int, input().split()))
ans = 0
for _ in range(k):
  m = min(p)
  ans += m
  p.remove(m)
  
print(ans)