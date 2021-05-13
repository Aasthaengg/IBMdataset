H, W = map(int,input().split())
N = int(input())
ans = [[0]*W for _ in range(H)]
A = [int(i) for i in input().split()]
hpos = 0
wpos = 0
apos = 0
cnt = 0
while True:
  while cnt<A[apos]:
    ans[hpos][wpos] = apos+1
    if hpos%2 == 0:
      wpos += 1
      if wpos == W:
        hpos += 1
        wpos = W-1
    else:
      wpos -= 1
      if wpos == -1:
        hpos += 1
        wpos = 0
    cnt += 1
  cnt = 0
  apos += 1
  if hpos == H:
    break
for i in range(H):
  print(*ans[i])