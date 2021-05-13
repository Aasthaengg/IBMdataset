import math
import sys

N = int(input())
A = list(map(int, input().split()))

li = [0] * N
count = 0

if N % 2 == 0:
  t = 1
else:
  t = 0

for a in A:
  if a == 0:
    li[math.floor((N-1)/2)] += 1
    count += 1
    
    if count == 2:
      print(0)
      sys.exit()

    continue

  li[math.floor((N-1)/2)-math.floor(a/2)] += 1
  li[math.floor((N-1)/2)+math.floor(a/2)+t] += 1

ans = 1

for i in range(0, math.floor(N/2)):
  ans *= li[i]

print(ans % (10**9 + 7))