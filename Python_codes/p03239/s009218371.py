n,t = map(int,input().split())
c_t = [list(map(int,input().split())) for _ in range(n)]
cost = [100000]
for i in range(n):
  if c_t[i][1] <= t:
    cost.append(c_t[i][0])
if min(cost) == 100000:
  print("TLE")
else:
  print(min(cost))