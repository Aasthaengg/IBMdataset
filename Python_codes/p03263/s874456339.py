import numpy as np
H, W=map(int, input().split())
A=[]
for i in range(H):
  A.append(list(map(int, input().split())))

B=[]
for i in range(H):
  if i%2==0:
    for j in range(W):
      B.append([A[i][j],i,j])
  else:
    for j in range(1,W+1):
      B.append([A[i][-j],i,W-j])
      
ans=[]


for i in range(len(B)-1):
  a,x,y=B[i][0], B[i][1], B[i][2]
  if a%2==1:
    B[i+1][0]+=1
    ans.append((x,y,B[i+1][1], B[i+1][2]))
print(len(ans))  
for a,b,c,d in ans:
  print(a+1,b+1,c+1,d+1)


