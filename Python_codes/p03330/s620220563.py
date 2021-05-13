N,C=map(int,input().split())
D=[[int(x) for x in input().split()] for y in range(C)]
c=[[int(x)-1 for x in input().split()] for y in range(N)]

d=[[0 for x in range(C)] for y in range(3)]
for i in range(N):
  for j in range(N):
    d[(i+j)%3][c[i][j]] += 1

a=10**9
for c0 in range(C):
  for c1 in range(c0+1,C):
    for c2 in range(c1+1,C):
      s1,s2,s3,s4,s5,s6=0,0,0,0,0,0
      for c in range(C):
        s1 += d[0][c]*D[c][c0]+d[1][c]*D[c][c1]+d[2][c]*D[c][c2]
        s2 += d[0][c]*D[c][c0]+d[1][c]*D[c][c2]+d[2][c]*D[c][c1]
        s3 += d[0][c]*D[c][c1]+d[1][c]*D[c][c0]+d[2][c]*D[c][c2]
        s4 += d[0][c]*D[c][c1]+d[1][c]*D[c][c2]+d[2][c]*D[c][c0]
        s5 += d[0][c]*D[c][c2]+d[1][c]*D[c][c0]+d[2][c]*D[c][c1]
        s6 += d[0][c]*D[c][c2]+d[1][c]*D[c][c1]+d[2][c]*D[c][c0]
      a=min(a,s1,s2,s3,s4,s5,s6)
print(a)
