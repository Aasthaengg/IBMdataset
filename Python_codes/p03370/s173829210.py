N,X = map(int, input().split())
M = [int(input()) for i in range(N)]
M.sort()
for i in range(N):
  X = X - M[i]
cnt = X//M[0]
print(N+cnt)