H,W=map(int,input().split())
Map=[]
for i in range(H):
  Map.append(input())
for i in range(H):
  for j in range(W):
    if Map[i][j]=='#':
      if i-1>=0 and i+1<H and j-1>=0 and j+1<W:
        if Map[i-1][j]!='#' and Map[i+1][j]!='#' and Map[i][j-1]!='#' and Map[i][j+1]!='#':
          print('No')
          exit()
print('Yes')