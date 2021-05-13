A=[list(map(int,input().split())) for _ in range(3)]
N=int(input())
b=[int(input()) for _ in range(N)]
G=[['*']*3,['*']*3,['*']*3]
for i in range(3):
  for j in range(3):
    if A[i][j] not in b:
      G[i][j]=A[i][j]

if G[0][0]==G[1][1]==G[2][2]=='*':
  print('Yes')
  exit()
elif G[0][2]==G[1][1]==G[2][0]=='*':
  print('Yes')
  exit()
else:
  for i in range(3):
    if G[i][0]==G[i][1]==G[i][2]=='*':
      print('Yes')
      exit()
    elif G[0][i]==G[1][i]==G[2][i]=='*':
      print('Yes')
      exit()

print('No')