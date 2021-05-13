H,W,A,B=map(int,input().split())
mat=[]
for _ in range(B):
  r='0'*A+'1'*(W-A)
  mat.append(r)

for _ in range(H-B):
  r='1'*A+'0'*(W-A)
  mat.append(r)

for i in range(H):
  print(mat[i])