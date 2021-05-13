N = int(input())
xy = [list(map(int,input().split())) for _ in range(N)]
if N == 1:
  print(1)
  exit()
d = []
for i in range(N):
  for j in range(N):
    if i == j:
      continue
    X = xy[i][0] - xy[j][0]
    Y = xy[i][1] - xy[j][1]
    d.append([X,Y])
d.sort()
#print(d)
cnt = 1
tmp = 1
std = d[0]
for i in range(1,len(d)):
  if d[i] == std:
    tmp += 1
  else:
    tmp = 1
  std = d[i]
  cnt = max(cnt,tmp)
print(N - cnt)