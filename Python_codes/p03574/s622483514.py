H,W = map(int, input().split())
T = []
T.append(["."]*(W+2))
for _ in range(H):
  s = "."+input()+"."
  T.append(list(s))
T.append(["."]*(W+2))
for h in range(1, H+1):
  for w in range(1, W+1):
    if T[h][w]==".":
      S = [T[a][b] for b in range(w-1, w+2) \
           for a in range(h-1, h+2)]
      T[h][w]=S.count("#")
for h in range(1, H+1):
  print(*T[h][1:W+1], sep="")