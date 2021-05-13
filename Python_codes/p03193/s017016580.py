N,H,W = map(int,input().split())
ans = 0
k = []
for i in range(N):
  k.append(list(map(int,input().split())))
for i in range(N):
  if k[i][0]>=H and k[i][1]>=W:
    ans += 1
print(ans)