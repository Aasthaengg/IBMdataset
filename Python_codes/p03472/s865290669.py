import bisect
import math

N, H = map(int, input().split())

am = 0
Bs = []

for _ in range(N):
  a,b = map(int, input().split())
  am = max(am, a)
  Bs.append(b)
  
Bs.sort()
j = bisect.bisect_right(Bs, am)

rlt = 0
for i in range(N-1, j-1, -1):
  H -= Bs[i]
  rlt += 1
  if H <= 0:
    break
    
if H > 0:
  rlt += math.ceil(H/am)
  
print(rlt)