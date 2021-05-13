S = input()
N = len(S)
db = [[0]*N for _ in range(20)]
db[0] =  [i+1 if S[i]=='R' else i-1 for i in range(N)]
for i in range(1,20):
  for j in range(N):
    db[i][j] = db[i-1][db[i-1][j]]
ans = [0]*N
for i in range(N):
  K = 10**5
  p = 0
  pos = i
  while K:
    if K%2:
      pos = db[p][pos]
    p += 1
    K >>= 1
  ans[pos] += 1
print(*ans)