N,T  = map(int,input().split())
ct = [list(map(int,input().split())) for _ in range(N)]

ans = 10**6
for n in range(N):
  if ct[n][1] <= T:
    if ct[n][0] <= ans:
      ans = ct[n][0]
if ans != 10**6:
  print(ans)
else:
  print("TLE")
