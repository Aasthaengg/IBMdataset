N,W,H=[int(i) for i in input().split()]

ans=0

for i in range(N):
  w,h=[int(x) for x in input().split()]
  if h>=H and w>= W:
    ans+=1

print(ans)
