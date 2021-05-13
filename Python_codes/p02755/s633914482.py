A, B = map(int, input().split())
import math

ans = -1

for i in range(13, 1001):
  if math.floor(i * 0.08) == A and math.floor(i * 0.1) == B :
    ans = i
    break

print(ans)