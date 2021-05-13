n = int(input())
table = [[0]*10 for _ in range(10)]
for i in range(1, n+1):
  start = int(str(i)[0])
  end = int(str(i)[-1])
  table[start][end] += 1

ans = 0
for i in range(10):
  for j in range(10):
    ans += table[i][j]*table[j][i]
print(ans)