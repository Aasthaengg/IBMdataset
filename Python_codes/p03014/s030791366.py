n,m = map(int, input().split())

S = [[] for _ in range(n)]

for i in range(n):
    S[i] = list(input())

rows = [[] for _ in range(n)]
cols = [[] for _ in range(m)]

start = [[] for _ in range(n)]
end = [[] for _ in range(n)]

for i in range(n):
    rows[i].append(-1)
    for j in range(m):
        if(S[i][j] == '#'):
            rows[i].append(j)
    rows[i].append(m)

    l = 0
    r = 1
    cnt = 0

    for j in range(m):
        if(S[i][j] != '#'):
            start[i].append(rows[i][r] - rows[i][l])
        else:
            start[i].append(0)
        if(j == rows[i][r]):
            l = r
            r = r + 1
ans = 0
for i in range(m):
    cols[i].append(-1)

    for j in range(n):
        if(S[j][i] == '#'):
            cols[i].append(j)
    cols[i].append(n)

    l = 0
    r = 1
    cnt = 0

    for j in range(n):
        if(S[j][i] != '#'):
            end[j].append(cols[i][r] - cols[i][l])
            # ans = max(ans, start[j][i], end[j][i])
        else:
            end[j].append(0)
        if(j == cols[i][r]):
            l = r
            r = r + 1
        



for i in range(n):
    for j in range(m):
        # if(S[i][j] != '#'):
            ans = max(ans, start[i][j] + end[i][j])

print(ans - 3)


