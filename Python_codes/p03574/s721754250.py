H, W = map(int,input().split())
S = [list(input()) for _ in range(H)]



for h in range(H):
  for w in range(W):

    if S[h][w] == ".":
      cnt = 0

      for h1 in range(max(0,h-1),min(H,h+2)):
        for w1 in range(max(0,w-1),min(W,w+2)):
          if S[h1][w1] =="#":
            cnt += 1
      S[h][w] = cnt
    
for h in range(H):
  print("".join(map(str,S[h])))