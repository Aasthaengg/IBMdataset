H,W=map(int, input().split()) 
S=[[0 for _ in range(W+2)] for _ in range(H+2)]
for i in range(H):
  S[i+1]= ["#"] + list(input()) + ["#"]
for j in range(W+2):
  S[0][j]="#"
  S[-1][j]="#"
  
t=[[-1 for _ in range(W)] for _ in range(H)]
y=[[-1 for _ in range(W)] for _ in range(H)]

for i in range(H):
  for j in range(W):
    if S[i+1][j+1]==".":
      if t[i][j]==-1:
        k=1
        while True:
          if S[i+k+1][j+1]==".":
            k +=1
          else:
            break
        for l in range(k):
          t[i+l][j]=k       
      if y[i][j]==-1:
        m=1
        while True:
          if S[i+1][j+1+m]==".":
            m +=1
          else:
            break
        for n in range(m):
          y[i][j+n]=m       

maxi=0          
for i in range(H):
  for j in range(W):
    maxi=max(maxi, t[i][j]+y[i][j])
print(maxi-1)