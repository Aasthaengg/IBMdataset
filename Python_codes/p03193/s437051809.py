N,H,W=map(int,input().split())
li=[map(int,input().split()) for _ in range(N)]
ans=0
for h,w in li:
  if h>=H and w>=W:
    ans+=1
print(ans)