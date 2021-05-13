n, k = map(int, input().split())
ans = 0
count = 0

if k == 1:
  print(1)
else:
  for i in range(1, n+1):
    while i < k:
      i *= 2
      count += 1
    ans = ans + 0.5**count/n
    count = 0
  
  print(ans)