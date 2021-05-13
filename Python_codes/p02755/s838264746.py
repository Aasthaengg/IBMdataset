a,b=map(int,input().split())

import math
limit = int(100 // 0.08 + 1)
for i in range(1,limit+1):
  v_a = i * 0.08
  v_b = i * 0.1
  if math.floor(v_a) == a and math.floor(v_b) == b:
    print(i)
    exit(0)

print(-1)
