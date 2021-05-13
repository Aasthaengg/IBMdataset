n, t = map(int, input().split())
C = 1111
for i in range(n):
  c, a = map(int, input().split())
  if a <= t:
    if c < C:
      C = c
if C == 1111:
  print("TLE")
else:
  print(C)