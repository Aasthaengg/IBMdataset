H,W = map(int,input().split())
S = [list(input()) for n in range(H)]
A = [["."]*(W+2)]*(H+2)

S.insert(0,(["."]*W))
S.append(["."]*W)

for h in range(H+2):
  S[h].insert(0,".")
  S[h].append(".")

for h in range(1,1+H):
  for w in range(1,1+W):
    ans=0
    if S[h][w]==".":
      ans+=S[h-1][w-1:w+2].count("#")
      ans+=S[h][w-1:w+2].count("#")
      ans+=S[h+1][w-1:w+2].count("#")
      S[h][w]=ans

for h in range(1,1+H):
  print(*S[h][1:-1],sep="")