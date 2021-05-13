H,W = map(int,input().split())
S = [(2+W)*"."]+["."+input()+"." for h in range(H)]+[(2+W)*"."]

for h in range(1,1+H):
  for w in range(1,1+W):
    if S[h][w]!="#":
      s = S[h-1][w-1:w+2]+S[h][w-1]+S[h][w+1]+S[h+1][w-1:w+2]
      S[h]=S[h][:w]+str(s.count("#"))+S[h][w+1:]

for h in range(1,1+H):
  print(S[h][1:1+W])