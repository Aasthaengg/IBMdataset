H,W,K = map(int,input().split())
C = [list(input()) for h in range(H)]
ans = 0

for h in range(2**H):
  for w in range(2**W):
    c = 0
    for i in range(H):
      for j in range(W):
        if (h>>i)&1==0 and (w>>j)&1==0 and C[i][j]=="#":
          c+=1
    if c==K:
      ans+=1

print(ans)