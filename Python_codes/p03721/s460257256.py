N,K = map(int,input().split())
ab = [list(map(int,input().split())) for _ in range(N)]
ab.sort()
count = 0

for i in range(N):
  a,b  = ab[i][0],ab[i][1]
  count += b
  if count >= K:
    print(a)
    break