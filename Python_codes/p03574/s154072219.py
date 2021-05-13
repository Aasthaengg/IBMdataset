h, w = map(int, input().split())

dp = [[0]*w for _ in range(h)]

for i in range(h):
  s = input()
  for j in range(w):
    if s[j] == '#':
      dp[i][j] = '#'
      for p in range(i-1, i+2):
        if p < 0 or h-1 < p:
          continue
        for q in range(j-1, j+2):
          if q < 0 or w-1 < q:
            continue
          elif dp[p][q] == '#':
            continue
          dp[p][q] += 1
      
for k in dp:
  print(*k, sep='')