n, w, h = map(int, input().split())
ans = 0

for _ in range(n):
  wi, hi = map(int, input().split())
  if wi >= w and hi >= h:
    ans += 1
    
print(ans)