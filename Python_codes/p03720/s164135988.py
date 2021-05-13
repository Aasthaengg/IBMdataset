N, M = map(int, input().split())
road = [0 for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    road[a-1] += 1; road[b-1] += 1

for i in range(N):
    print(road[i])