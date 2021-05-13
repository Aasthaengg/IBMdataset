N, M = map(int, input().split())
ab = []
cd = []
for i in range(N):
  tmp = list(map(int, input().split()))
  ab.append(tmp)
for j in range(M):
  tmp = list(map(int, input().split()))
  cd.append(tmp)
for i in range(N):
  tmp = 10**10
  tmp2 = 0
  for j in range(M):
    if tmp > abs(ab[i][0]-cd[j][0])+abs(ab[i][1]-cd[j][1]):
      tmp = abs(ab[i][0]-cd[j][0])+abs(ab[i][1]-cd[j][1])
      tmp2 = j
  print(tmp2+1)