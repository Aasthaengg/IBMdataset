H,W = map(int,input().split())
 
ans = []
 
dp = [ list ( map(int,input().split()) )  for i in range(H)]
 
for i in range(H):
  for j in range(W):
    a = dp[i][j]
    if j != W -1:
      if a %  2 == 1:
        dp[i][j+1] += 1
        ans.append([i+1,j+1,i+1,j+2])
    elif i != H-1:
      if a % 2 == 1:
        dp[i+1][j] += a
        ans.append([i+1,j+1,i+2,j+1])
      
print(len(ans))
for i in range(len(ans)):
  print(ans[i][0],ans[i][1],ans[i][2],ans[i][3])