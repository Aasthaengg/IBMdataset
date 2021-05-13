import itertools
N,K=map(int,input().split())
XY=[list(map(int,input().split())) for i in range(N)]
ans=float("inf")

for xv in itertools.combinations( [xy[0] for xy in XY] ,2):
  for yv in itertools.combinations( [xy[1] for xy in XY] ,2):
    xmax=max(xv[0],xv[1])
    xmin=min(xv[0],xv[1])
    ymax=max(yv[0],yv[1])
    ymin=min(yv[0],yv[1])

    k=0
    for xy in XY:
      x,y=xy[0],xy[1]
      if xmin<=x and x<=xmax:
        if ymin<=y and y<=ymax:
          k+=1    
    if k>=K:
      ans=min(ans,(xmax-xmin)*(ymax-ymin))
print(ans)