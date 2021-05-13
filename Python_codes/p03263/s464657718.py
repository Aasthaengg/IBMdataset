H, W = map(int, input().split())
a = [list(map(int, input().split())) for i in range(H)]
c = 0
N = 0
ans = []
for i in range(H):
  for j in range(W):
    if a[i][j]%2==1:
      if j+1<W:
        ans.append([i+1,j+1,i+1,j+2])
        a[i][j]-=1
        a[i][j+1]+=1
        N += 1
      elif i+1<H:
        a[i][j]-=1
        a[i+1][j]+=1
        ans.append([i+1,j+1,i+2,j+1])
        N += 1
    
        
print(N)
for i in range(N):
  L=[str(x) for x in ans[i]]
  L=" ".join(L)
  print(L)
  
