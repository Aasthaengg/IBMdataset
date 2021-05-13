H, W = map(int,input().split())
S = [list(input()) for _ in range(H)]

ans = "Yes"
for h in range(H):
  for w in range(W):
    if S[h][w] == "#":
      flag = 0
      
      if h == 0:
        h1 = [1]
      elif h == H-1:
        h1 = [H-2]
      else:
        h1 = [h-1,h+1]
      
      if w == 0:
        w1 = [1]
      elif w == W-1:
        w1 = [W-2]
      else:
        w1 = [w-1,w+1]
        
      for h0 in h1:
        if S[h0][w] =="#":
          flag = 1
          
      for w0 in w1:
        if S[h][w0] == "#":
          flag = 1
       
      if flag == 0:
        ans = "No"
        break
print(ans)