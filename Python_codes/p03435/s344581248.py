c=[list(map(int,input().split())) for _ in range(3)]

for j in range(2):
  for i in range(3):
    if i==0:
      d = c[i][j+1]-c[i][j]
    else:
      if c[i][j+1]-c[i][j] != d:
        print('No')
        exit()

for i in range(2):
  for j in range(3):
    if j==0:
      d = c[i+1][j]-c[i][j]
    else:
      if c[i+1][j]-c[i][j] != d:
        print('No')
        exit()
print('Yes')