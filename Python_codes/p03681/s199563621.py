import math
N,M = map(int,input().split())
n = max(N,M)
m = min(N,M)
if abs(N-M) > 1:
  print(0)
  exit()
 
ncnt = math.factorial(n) % 1000000007
 
if abs(N-M) == 0:
  mcnt = 2 * ncnt
else:
  mcnt = math.factorial(m)
print(ncnt*mcnt % 1000000007)