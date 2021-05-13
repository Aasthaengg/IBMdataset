n, c = map(int, input().split())
MAX_COLS = 10**5
table = [[0 for _ in range(MAX_COLS)] for _ in range(c)]

for _ in range(n):
    s, t, i = list(map(int, input().split()))
    for j in range(s - 1, t - 1):
        table[i - 1][j] = 1

for i in range(c):
    for j in range(MAX_COLS - 1):
        if table[i][j] == 0 and table[i][j + 1] == 1:
            table[i][j] = 1

res = 0
for j in range(MAX_COLS):
    count = 0
    for i in range(c):
        count += table[i][j]
    res = max(res, count)
print(res)