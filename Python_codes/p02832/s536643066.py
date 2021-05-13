N = int(input())
blocks = list(map(int, input().split()))
target = 1
for block in blocks:
  if block == target:
    target += 1
if target > 1:
  print(N-target+1)
else:
  print(-1)
