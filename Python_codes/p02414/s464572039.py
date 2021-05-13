n,m,l=(int(x) for x in input().split())
a=[[0 for i in range(m)] for j in range(n)]
b=[[0 for i in range(l)] for j in range(m)]
c=[[0 for i in range(l)] for j in range(n)]

for i in range(n):
  a[i][:]=(int(x) for x in input().split())

for i in range(m):
  b[i][:]=(int(x) for x in input().split())

for i in range(n):
  for j in range(m):
    for k in range(l):
      c[i][k]+=a[i][j]*b[j][k]

for i in range(n):
  for j in range(l):
    print(c[i][j],end='')
    if j<l-1:
      print(' ',end='')
  print('')
