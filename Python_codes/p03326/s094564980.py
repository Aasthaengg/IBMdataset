from itertools import product
N, M = map(int,input().split())
cakes = []
for _ in range(N):
    cakes.append(list(map(int,input().split())))
ans = 0
for i, j, k in product([-1,1], repeat = 3):
    L = []
    for x, y, z in cakes:
        L.append(i * x + j * y + k * z)
    L.sort(reverse = True)
    ans = max(ans, sum(L[:M]))
    L.clear()
print(ans)