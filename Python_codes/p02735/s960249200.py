H,W=map(int,input().split());M=[input()for _ in"_"*H];D=[[0]*-~W for _ in"_"*-~H];m=999
for i in range(H):
  for j in range(W):D[i+1][j+1]=min([m,D[i][j+1]+(M[i-1][j]>M[i][j])][i>0],[m,D[i+1][j]+(M[i][j-1]>M[i][j])][j>0],m*(i+j>0))
print(D[-1][-1]+(M[0][0]<".")) 