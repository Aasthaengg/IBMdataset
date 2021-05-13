N = int(input())

l = [[0]*10 for i in range(10)]
for i in range(1, N+1):
  x = int(str(i)[0])
  y = int(str(i)[-1])
  l[x][y] += 1
  
ans = 0
for i in range(1, 10):
  for j in range(i, 10):
    if i == j:
      ans += l[i][j] * l[j][i]
    else:
      ans += 2 * l[i][j] * l[j][i]
print(ans)