n, m, q = map(int, input().split())

trains = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    l, r = map(int, input().split())
    trains[l][r] += 1

# cum
for i in range(n + 1):
    for j in range(n):
        trains[i][j + 1] += trains[i][j]

for i in range(n):
    for j in range(n + 1):
        trains[i + 1][j] += trains[i][j]

query = []
for _ in range(q):
    a, b = map(int, input().split())
    ans = trains[b][b] - trains[b][a - 1] - trains[a - 1][b] + trains[a - 1][a - 1]
    print(ans)