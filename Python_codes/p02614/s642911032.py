import itertools

H,W,K=map(int,input().split())
G = [input() for i in range(H)]

ans = 0
for i in itertools.product(range(2),repeat=H):
  for j in itertools.product(range(2),repeat=W):
    black = 0
    for h in range(H):
      for w in range(W):
        if i[h] == 0 and j[w] == 0 and G[h][w] == '#':
          black += 1
    ans += (black == K)

print(ans)