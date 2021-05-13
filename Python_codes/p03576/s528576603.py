N,K=map(int,input().split())
xy=[list(map(int,input().split())) for _ in range(N)]

X=sorted([i[0] for i in xy])
Y=sorted([i[1] for i in xy])

ans=[]
for i in range(N-1):
  lx=X[i]
  for j in range(i+1,N):
    rx=X[j]
    for k in range(N-1):
      dy=Y[k]
      for l in range(k+1,N):
        uy=Y[l]
        cnt=0
        for x,y in xy:
          if lx<=x and x<=rx and dy<=y and y<=uy:
            cnt+=1
        if cnt>=K:
          ans.append((rx-lx)*(uy-dy))
          
          
print(min(ans))