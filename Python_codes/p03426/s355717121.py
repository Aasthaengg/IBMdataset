H,W,D = map(int,input().split())
posi = [[]] * (H * W)

for _ in range(H):
  a = list(map(int,input().split()))
  for i,j in enumerate(a):
    posi[j - 1] = [_ + 1,i + 1]

Q = int(input())

acdist = [0] * (H * W)

for _ in range(0,H * W - D):
  acdist[_ + D] += acdist[_] + abs(posi[_ + D][0] - posi[_][0]) + abs(posi[_ + D][1] - posi[_][1])

for i in range(Q):
  l,r = map(int,input().split())
  print(acdist[r - 1] - acdist[l - 1])