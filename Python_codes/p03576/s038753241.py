import itertools
N,K = map(int,input().split())
zahyou = []
for i in range(N):
  zahyou.append(list(map(int,input().split())))
ans = float('inf')
X = []
Y = []
for i in range(N):
  X.append(zahyou[i][0])
  Y.append(zahyou[i][1])
P = list(itertools.combinations(X,2))
Q = list(itertools.combinations(Y,2))
for i in range(len(P)):
  for j in range(len(Q)):
    x1 = min(P[i][0],P[i][1])
    x2 = max(P[i][0],P[i][1])
    y1 = min(Q[j][0],Q[j][1])
    y2 = max(Q[j][0],Q[j][1])
    cnt = 0
    for k in range(N):
      if x1 <= zahyou[k][0] <= x2 and y1 <= zahyou[k][1] <= y2:
        cnt += 1
    if cnt >= K:
      if ans >= (x2-x1)*(y2-y1):
        ans = (x2-x1)*(y2-y1)
print(ans)
