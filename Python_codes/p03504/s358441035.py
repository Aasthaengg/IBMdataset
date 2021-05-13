N, C = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

LEN = 10 ** 5 + 7
d = [[0] * LEN for _ in range(C + 1)]
for s, t, c in X:
    d[c][s] += 1
    d[c][t + 1] -= 1

for i in range(C + 1):
    for j in range(LEN - 1):
        d[i][j + 1] += d[i][j]

x = [0] * LEN
for i in range(C + 1):
    for j in range(LEN):
        x[j] += int(d[i][j] > 0)
        
print(max(x))
