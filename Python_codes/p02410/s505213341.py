n,m=map(int,input().split())
A=[list(map(int,input().split())) for i in range(n)]
B=[int(input())for i in range(m)]


for i in range(n):
  kotae=0
  for j in range(m):
    kotae+=A[i][j]*B[j]
  print(kotae)
