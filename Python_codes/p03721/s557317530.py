N, K = map(int, input().split())
now = 0
ab = [list(map(int, input().split())) for _ in range(N)]
ab = sorted(ab)
for a, b in ab:
  if now < K <= now+b:
    print(a)
    exit()
  now += b