N, K = map(int, input().split())
L = [list(map(int,input().split())) for _ in range(N)]
M = sorted(L, key= lambda x:x[0])
count = 0
ans = 0
for i in range(N):
  ans = M[i][0]
  count += M[i][1]
  if (count >=K ):
    break
print(ans)