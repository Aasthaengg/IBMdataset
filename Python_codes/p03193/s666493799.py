from math import floor
N, H, W = map(int, input().split())
ans = 0
 
for i in range(N):
  A, B = map(int, input().split())
  if (A//H) * (B//W) > 0:
    ans += 1
  
print(ans)