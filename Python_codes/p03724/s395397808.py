N, M = map(int, input().split())
ab = []
for _ in range(M):
    ab.append(tuple(map(int, input().split())))

edges = [0] * N
for el in ab:
    a = min(el)
    b = max(el)
    edges[a - 1] += 1
    edges[b - 1] -= 1
# print(edges)
for i in range(1, N):
    edges[i] = edges[i] + edges[i - 1]

# print(edges)
if all([x % 2 == 0 for x in edges]):
    print('YES')
else:
    print('NO')