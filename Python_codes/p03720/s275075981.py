N, M = map(int, input().split())
route = {i: 0 for i in range(N)}
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    route[a] += 1
    route[b] += 1
route = (x[1] for x in sorted(route.items(), key=lambda x: x[0]))
print(*route, sep='\n')
