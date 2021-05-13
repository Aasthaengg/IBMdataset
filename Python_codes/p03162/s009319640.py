n=int(input())
a,b,c=[],[],[]
for i in range(n):
  a1,b1,c1=map(int,input().split())
  a+=[a1]
  b+=[b1]
  c+=[c1]

hp=[[0 for j in range(n)]for i in range(3)]
hp[0][0],hp[1][0],hp[2][0]=a[0],b[0],c[0]

for j in range(1,n):
  for i in range(3):
    
    if i==0:
      hp[i][j]+=max(hp[(2)][j-1],hp[(1)][j-1])+a[j]
    elif i==1:
      hp[i][j]+=max(hp[(0)][j-1],hp[(2)][j-1])+b[j]
    else:
      hp[i][j]+=max(hp[(1)][j-1],hp[(0)][j-1])+c[j]
    
    #print(i,j,hp[i][j])

#print(hp)
print(max(hp[0][n-1],hp[1][n-1],hp[2][n-1]))