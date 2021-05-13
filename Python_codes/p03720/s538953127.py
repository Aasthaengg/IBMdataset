N, M = map(int, input().split())
route = [[0 for i in range(N)] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    route[a-1][b-1] += 1
    route[b-1][a-1] += 1
for i in route:
    print(sum(i))
