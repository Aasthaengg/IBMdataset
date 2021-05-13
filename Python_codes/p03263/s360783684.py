H,W=map(int,input().split())
mat=[]
for i in range(H):
  line=list(map(int,input().split()))
  mat.append(line)
  
#print(mat)
oplist=[]
for i in range(H):
  for j in range(W):
    if mat[i][j]%2==1:
      if i==H-1 and j==W-1:
        break
      if j==W-1:
        mat[i][j]-=1
        mat[i+1][j]+=1
        oplist.append([i+1,j+1,i+2,j+1])
      else:
        mat[i][j]-=1
        mat[i][j+1]+=1
        oplist.append([i+1,j+1,i+1,j+2])
        
print(len(oplist))
for op in oplist:
  op_str=map(str,op)
  print(" ".join(op_str))