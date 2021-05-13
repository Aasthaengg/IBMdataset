n, t = map(int, input().split())
minN = 10000
for i in range(n):
  c, ti = map(int, input().split())
  if t >= ti and minN > c:
    minN = c
print("TLE" if minN == 10000 else minN)