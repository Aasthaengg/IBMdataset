H, W = map(int, input().split())
a = []
for i in range(H):
  a.append(list(map(int, input().split())))
  
tmp = []
for i in range(H):
  if (sum(a[i])%2==1) and (i<H-1):
    for j in range(W):
      if a[i][j] % 2 == 1:
        n = j
        a[i][j] -= 1
        a[i+1][0] += 1
        break
    for j in range(n):
      tmp.append([i+1, n-j+1, i+1, n-j])
    tmp.append([i+1, 1, i+2, 1])
  for j in range(W):
    if (a[i][j]%2==1) and (j<W-1):
      a[i][j] -= 1
      a[i][j+1] += 1
      tmp.append([i+1, j+1, i+1, j+2])
print(len(tmp))
for i in range(len(tmp)):
  print(*tmp[i])