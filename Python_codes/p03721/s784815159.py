N, K = map(int, input().split())
l = [tuple(map(int, input().split())) for _ in range(N)]
l.sort(key=lambda x: x[0])

cnt = 0
for x in l:
  cnt += x[1]
  if cnt >= K:
    print(x[0])
    break