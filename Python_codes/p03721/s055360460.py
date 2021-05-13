N, K = map(int, input().split())
ab = [[int(i) for i in input().split()] for _ in range(N)]

ab.sort()
c = 0
for i in range(N):
    c += ab[i][1]
    if c >= K:
        print(ab[i][0])
        break
