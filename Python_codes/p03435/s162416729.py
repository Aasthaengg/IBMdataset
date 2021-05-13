C=[list(map(int,input().split())) for i in range(3)]
B=[C[0][0],C[0][1],C[0][2]]
A=[0,C[1][0]-B[0],C[2][0]-B[0]]
for i in range(3):
  for j in range(3):
    if C[i][j] != A[i]+B[j]:
      print("No")
      quit()
print("Yes")