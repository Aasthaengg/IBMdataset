N,M = map(int,input().split())
c = []
for i in range(M):
  c.extend(list(map(int,input().split())))
for j in range(N):
  print(c.count(j+1))