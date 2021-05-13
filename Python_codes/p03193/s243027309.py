N,H,W = map(int,input().split())
L = []
for i in range(N):
  L.append(list(map(int,input().split())))
cnt = 0
for i in range(N):
  if L[i][0] >= H and L[i][1] >= W:
    cnt += 1
print(cnt)