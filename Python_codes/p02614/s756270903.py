h, w, k = map(int, input().split())
c = []
for i in range(h):
  c.append(list(input()))

ans = 0

for row in range((1 << h) - 1): #2^h - 1
  for col in range((1 << w) - 1): #2^w -1
    black = 0
    for i in range(h):
      for j in range(w):
        if (row >> i) & 1 == 0 and (col >> j) & 1 == 0 and c[i][j] =='#':
           black += 1
    if black == k:
      ans += 1

print(ans)
