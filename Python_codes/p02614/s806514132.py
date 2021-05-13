H, W, K = map(int, input().split())
C = []
for _ in range(H): C.append([c for c in input()])
ans = 0
for i in range(1<<H):
   for j in range(1<<W):
       cnt = 0
       for m in range(H):
           for n in range(W):
               if i>>m&1: continue
               if j>>n&1: continue
               if C[m][n] == '#': cnt += 1
       if cnt == K: ans += 1
print(ans)