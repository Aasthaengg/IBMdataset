n,m = map(int,input().split())

ab = [0]*m

for i in range(0,m):
  ab[i] = input().split()

to = [0]*n
d = [0]*2
for i in range(0,m):
  d[0] = int(ab[i][0])
  d[1] = int(ab[i][1])
  to[d[0]-1] += 1
  to[d[1]-1] += 1

for i in range(len(to)):
  print(to[i])