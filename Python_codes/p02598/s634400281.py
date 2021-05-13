import math

N, K = map(int, input().split())
As = list(map(int, input().split()))

r = max(As)

if K == 0:
  print(r)
  exit()
  
l = 1

while l < r:
  mid = (r + l)//2
  cnt = 0
  for a in As:
    cnt += math.ceil(a/mid) - 1
  if cnt <= K:
    r = mid
  else:
    l = mid + 1
  
print(r)