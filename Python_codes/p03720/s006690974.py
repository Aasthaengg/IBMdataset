N, M = map(int, input().strip().split(" "))

road = [[0]*N for i in range(N)]

for _ in range(M):
    a, b = map(int, input().strip().split(" "))
    road[a-1][b-1] += 1
    road[b-1][a-1] += 1

for i in range(N):
    print(sum(road[i]))
