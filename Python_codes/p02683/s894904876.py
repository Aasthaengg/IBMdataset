n,m,x = map(int,input().split())
ca = [[0]]*n
for i in range(n):
  ca[i] = list(map(int,input().split()))
minc = 10**10
for b in range(2**n):
  r = [0]*m
  c = 0
  for i in range(n):
    if b & (1<<i)>0:
      c += ca[i][0]
      for j in range(m):
        r[j] += ca[i][j+1]
  flag = True
  for j in range(m):
    if r[j] < x:
      flag = False
  if flag:
    minc=min(c,minc)
if minc < 10**9:
  print(minc)
else:
  print(-1)
  
      
