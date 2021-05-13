import sys
readline = sys.stdin.readline

N,H,W = map(int,readline().split())
ans = 0
for i in range(N):
  a,b = map(int,readline().split())
  if a >= H and b >= W:
    ans += 1
print(ans)