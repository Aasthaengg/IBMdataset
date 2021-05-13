h, w, k = map(int,input().split())
c = [0] * h
ans = 0

for i in range(h):
  c[i] = input()

for rows in range(1 << h):
  for cols in range(1 << w):
    black = 0
    for i in range(h):
      if (rows >> i) % 2 == 1:
        continue
      for j in range(w):
        if (cols >> j) % 2 == 1:
          continue
        if c[i][j] == '#':
          black += 1
    if black == k:
      ans += 1

print(ans)