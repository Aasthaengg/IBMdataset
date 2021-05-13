N,M = map(int,input().split())
sts = [list(map(int, input().split())) for i in range(N)]
checkp = [[i+1]+list(map(int, input().split())) for i in range(M)]
rt = [None] * N
distances = [2*(10**8)] * N
for s in range(N):
  for c in checkp:
    dist = abs(sts[s][0]-c[1]) + abs(sts[s][1]-c[2])
    if rt[s] is None:
      rt[s] = c[0]
      distances[s] = dist
    else:
      if distances[s] > dist:
        rt[s] = c[0]
        distances[s] = dist
for i in rt:
  print(i)