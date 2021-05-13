N,K=map(int,input().split())
ab = [tuple(map(int,input().split())) for _ in range(N)]

ab = sorted(ab)
cum = 0
for i in range(N):
  cum += ab[i][1]
  if cum >= K:
    print(ab[i][0])
    exit()