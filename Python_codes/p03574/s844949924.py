h,w = map(int, input().split())
s = [list(input()) for _ in range(h)]

ans = [[0]*w for _ in range(h)]
for i in range(h):
  for j in range(w):
    if s[i][j] == "#":
      ans[i][j] = "#"
      for i2 in range(i-1, i+2):
        if i2 < 0 or h-1 < i2: continue
        for j2 in range(j-1, j+2):
          if (j2 < 0 or w-1 < j2): continue
          elif ans[i2][j2] == "#": continue
          ans[i2][j2] += 1
for i in ans:
  print("".join(map(str,i)))