A=[input().split() for _ in range(3)]
N=int(input())
B=[input() for _ in range(N)]

for i in range(3):
  for j in range(3):
    if A[i][j] in B:
      A[i][j]=0

if A[0][0]==A[1][1]==A[2][2] or A[0][2]==A[1][1]==A[2][0]:
  print("Yes")
  exit()

for n in range(3):
  if A[0][n]==A[1][n]==A[2][n] or A[n][0]==A[n][1]==A[n][2]:
    print('Yes')
    exit()

print('No')