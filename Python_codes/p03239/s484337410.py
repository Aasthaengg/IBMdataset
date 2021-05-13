N, T = map(int, input().split())
ans = 10000
for i in range(N):
  c, t = map(int, input().split())
  if t <= T:
    ans = min(ans, c)
print("TLE" if ans == 10000 else ans)