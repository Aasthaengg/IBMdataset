n, m, l = map(int, input().split())
a = [[] for _ in range(n)]
b = [[] for _ in range(m)]
 
for i in range(n):
  a[i] = list(map(int, input().split()))
 
for i in range(m):
  b[i] = list(map(int, input().split()))
 
for i in range(n):
  line = []
  
  for j in range(l):
    c = 0
    
    for k in range(m):
      c += a[i][k]*b[k][j]
    
    line.append(str(c))

  print(' '.join(line))
