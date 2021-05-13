N = int(input())
pnt = [[0]*3]
for i in range(N):
  pnt.append(list(map(int, input().split())))
cnt = 0
for i in range(1, N+1):
  t = pnt[i][0] - pnt[i-1][0]
  x = abs(pnt[i][1] - pnt[i-1][1])
  y = abs(pnt[i][2] - pnt[i-1][2])
  if t >= x+y and (t-(x+y)) % 2 == 0:
    cnt += 1
if cnt == N: print("Yes")
else: print("No")
