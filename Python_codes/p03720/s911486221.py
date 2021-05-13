N, M = map(int, input().split())
route = [0] * N
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    route[a] += 1
    route[b] += 1
print(*route, sep='\n')
