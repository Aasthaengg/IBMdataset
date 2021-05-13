N = int(input())
T = list(map(int, input().split()))
M = int(input())
X = [list(map(int, input().split())) for i in range(M)]
ans = [sum(T)]*M
for i in range(M):
  ans[i] += (X[i][1]-T[X[i][0]-1])
for i in range(M):
  print(ans[i])
