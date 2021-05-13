n,t = map(int, input().split())
min_ = 10**18
for i in range(n):
  c,t2 = map(int, input().split())
  if t>=t2:
    min_ = min(min_, c)
if min_ == 10**18:
  print("TLE")
else:
  print(min_)