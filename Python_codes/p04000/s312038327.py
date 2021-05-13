from collections import defaultdict

H,W,N = map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(N)]

Cells = defaultdict(int)
Count = [(H-2)*(W-2)] + [0 for _ in range(9)]

for a,b in AB:
  a -= 1
  b -= 1
  for i in range(-1,2):
    for j in range(-1,2):
      if 1 <= a+i <= H-2 and 1 <= b+j <= W-2:
        Count[Cells[(a+i,b+j)]] -= 1
        Count[Cells[(a+i,b+j)]+1] += 1
      Cells[(a+i,b+j)] += 1
for c in Count:
  print(c)