N, M = (int(x) for x in input().split())
L = []
for i in range(N):
  A, B = (int(x) for x in input().split())
  L.append((A,B))
L.sort()
tn = 0
tm = 0
for i in range(N):
  if L[i][1] < M-tn:
    tn += L[i][1]
    tm += L[i][0]*L[i][1]
  else:
    tm += L[i][0]*(M-tn)
    print(tm)
    quit()