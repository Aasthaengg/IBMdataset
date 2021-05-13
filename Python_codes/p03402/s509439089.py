A,B=map(int,input().split())

mat=[]
for i in range(100):
  array=["."]*50+["#"]*50
  mat.append(array)

for i in range(B-1):
  j=2*(i//25)
  k=2*(i%25)
  mat[j][k]="#"
for i in range(A-1):
  j=2*(i//25)
  k=2*(i%25)+51
  mat[j][k]="."
  
print(100,100)
for i in range(100):
  print("".join(mat[i]))