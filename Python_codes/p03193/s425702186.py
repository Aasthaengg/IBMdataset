N,H,W=map(int,input().split())
AB=[list(map(int,input().split())) for i in range(N)]
ans=0
for i in range(N):
  if AB[i][0]>=H and AB[i][1]>=W:
    ans+=1
print(ans)