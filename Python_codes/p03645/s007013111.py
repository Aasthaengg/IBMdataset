N, M = map(int, input().split())
route_1 = [0] * (N+1)
route_n = [0] * (N+1)

for i in range(M):
    a, b = map(int, input().split())
    if a == 1:
        route_1[b] = 1
    elif b == N:
        route_n[a] = 1

for i in range(2, N+1):
    if route_1[i] == 1 and route_n[i] == 1:
        print('POSSIBLE')
        exit()
print('IMPOSSIBLE')
