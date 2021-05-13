l, m, n = map(int,input().split())
a = [[0 for i in range(m)] for i in range(l)]
b = [[0 for i in range(n)] for i in range(m)]
c = [[0 for i in range(n)] for i in range(l)]

for i in range(l):
 a[i] = [int(x) for x in input().split()]

for i in range(m):
 b[i] = [int(x) for x in input().split()]

for i in range(l):
 for j in range(n):
  for k in range(m):
   c[i][j] += (a[i][k] * b[k][j])
 print(" ".join([str(x) for x in c[i]]))