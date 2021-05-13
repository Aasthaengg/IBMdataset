h,w = map(int, input().split())
s = [input() for _ in range(h)]

nums = [[] for _ in range(h)]
for i in range(h):
  for j in range(w):
    if s[i][j] == "#": nums[i].append("#")
    else:
      t = 0
      for a in range(i-1, i+2):
        if a < 0 or h <= a: continue
        for b in range(j-1, j+2):
          if b < 0 or w <= b: continue
          if s[a][b] == "#": t += 1
      nums[i].append(t)

for i in nums: print(*i, sep="")