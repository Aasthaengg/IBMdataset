n,m = map(int, input().split())

R = [list(map(int,input().split())) for i in range(m)]

X = []
for i in range(m):
  X.append(R[i][0])
  X.append(R[i][1])
  
for i in range(1,n+1):
  print(X.count(i))