n, timelimit = map(int, input().split() )
ans = 1001
for i in range (n):
  cost, time = map(int, input().split() )
  if time <= timelimit:
    ans = min(ans, cost)
print (ans if ans <= 1000 else "TLE")