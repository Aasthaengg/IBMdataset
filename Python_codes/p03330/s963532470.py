N,C=map(int,input().split())
D=[[int(x) for x in input().split()] for y in range(C)]
c=[[int(x)-1 for x in input().split()] for y in range(N)]

d=[[0 for x in range(C)] for y in range(3)]
for i in range(N):
  for j in range(N):
    d[(i+j)%3][c[i][j]] += 1

a=10**9
for c0 in range(C):
  for c1 in range(C):
    for c2 in range(C):
      if c0==c1 or c1==c2 or c0==c2:
        continue
      s=0
      for c in range(C):
        s += d[0][c]*D[c][c0]+d[1][c]*D[c][c1]+d[2][c]*D[c][c2]
      a=min(a,s)
print(a)
