H,W=map(int,input().split())
x=[[] for _ in range(H)]
xn=[[] for _ in range(H)]
for i in range(H):
  for _ in range(W):
    xn[i].append(999)

for i in range(H):
  x[i]=input()

xn[0][0]=0

for i in range(H+W-1):
  for j in range(i+1):
    if i-j>=W:
      continue
    if j>=H:
      break
    
    w=1
    h=1
    if i-j>=W-1:
      w=0
    if j>=H-1:
      h=0
    if w==1:
      if x[j][i-j]==".":
        if x[j][i-j+1]=="#":
          xn[j][i-j+1]=min(xn[j][i-j]+1,xn[j][i-j+1])
        else:
          xn[j][i-j+1]=min(xn[j][i-j],xn[j][i-j+1])
      else:
        xn[j][i-j+1]=min(xn[j][i-j],xn[j][i-j+1])
    if h==1:
      if x[j][i-j]==".":
        if x[j+1][i-j]=="#":
          xn[j+1][i-j]=min(xn[j][i-j]+1,xn[j+1][i-j])
        else:
          xn[j+1][i-j]=min(xn[j][i-j],xn[j+1][i-j])
      else:
        xn[j+1][i-j]=min(xn[j][i-j],xn[j+1][i-j])

if x[0][0]=="#":
  xn[H-1][W-1]+=1
print(xn[H-1][W-1])