N, C = map(int, input().split())
table = [[] for _ in range(C)]
for i in range(N):
    s, t, c = map(int, input().split())
    c -= 1
    table[c].append([s, t])

for i in range(C):
    table[i].sort()
    for j in range(len(table[i])-1):
        if table[i][j][1] == table[i][j+1][0]:
            table[i][j+1][0] = table[i][j][0]
            table[i][j] = [-1, -1]

imos = [0] * (10 ** 5 + 1000)
for channel in table:
    for s, t in channel:
        if s + t < 0:
            continue
        imos[s] += 1
        imos[t+1] -= 1

for i in range(10 ** 5 + 10):
    imos[i+1] += imos[i]

print(max(imos))
