N,M = map(int,input().split())
ab = [list(map(int,input().split())) for _ in range(M)]

ans = [0 for _ in range(N)]

for m in range(M):
  ans[ab[m][0]-1] += 1
  ans[ab[m][1]-1] += 1

for a in ans:
  print(a)