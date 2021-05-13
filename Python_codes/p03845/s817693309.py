N = int(input())
T = list(map(int, input().split()))
M = int(input())
PX = [list(map(int, input().split())) for _ in range(M)]

Tsum = sum(T)
for i in range(M):
  sa = T[PX[i][0]-1] - PX[i][1]
  print(Tsum - sa)
