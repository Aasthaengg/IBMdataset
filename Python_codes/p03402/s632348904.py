K = 50
A, B = map(int, input().split())
grid = [[0]*(2*K) for i in range(2*K)]
for i in range(K):
  grid[i] = [1]*(2*K)

row = 0
while A>1:
  if row%2==0:
    if A>K:
      grid[row] = [1,0]*K
      A -= K
    else:
      grid[row] = [1,0]*(A-1)+[1,1]*(K-A+1)
      break
  row += 1

row = K+1
while B>1:
  if row%2==0:
    if B>K:
      grid[row] = [1,0]*K
      B -= K
    else:
      grid[row] = [1,0]*(B-1)+[0,0]*(K-B+1)
      break
  row += 1

ans = []
for i in range(2*K):
  s = ''
  for j in range(2*K):
    if grid[i][j] == 1:
      s += '#'
    else:
      s += '.'
  ans += [s]
print(2*K,2*K)
for i in range(2*K):
  print(ans[i])