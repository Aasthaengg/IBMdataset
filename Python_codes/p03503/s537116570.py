N = int(input())
F = list()
P = list()
ans = - 10**10
for i in range(N):
  F.append(list(map(int, input().split())))
for i in range(N):
  P.append(list(map(int, input().split())))
for i in range(1, 1<<10):
  shop = list()
  cnt = [0]*N
  tmp = 0
  for j in range(10):
    if i>>j & 1:
      shop.append(j)
  for s in range(N):
    for p in shop:
      if(F[s][p] == 1):
        cnt[s] += 1
    tmp += P[s][cnt[s]]
  ans = max(ans, tmp)
print(ans)