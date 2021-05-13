N, K = map(int, input().split())
A = list(map(lambda x:int(x)-1, input().split()))
db = [[0]*N for _ in range(60)]
db[0] = A[:]
for i in range(1,60):
  for j in range(N):
    db[i][j] = db[i-1][db[i-1][j]]
ans = p = 0
while K>0:
  if K%2==1:
    ans = db[p][ans]
  p += 1
  K >>= 1
print(ans+1)
