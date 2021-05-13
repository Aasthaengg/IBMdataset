data = input().rstrip().split()
mat=[[1 for i in range(int(data[1]))] for j in range(int(data[0]))]
n = input().rstrip().split()
#print(mat)
for i2 in range(int(n[0])):
  for k in range(int(data[1])):
    mat[i2][k]=0
#print(mat)
for j2 in range(int(n[1])):
  for k in range(int(data[0])):
    mat[k][j2]=0
ans=0
for l in range(len(mat)):
  ans+=sum(mat[l])
print(ans)