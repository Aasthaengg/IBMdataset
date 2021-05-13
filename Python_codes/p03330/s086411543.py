n, c = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(c)]
s = [list(map(int, input().split())) for _ in range(n)]
c0 = [[0 for _ in range(c)] for _ in range(3)]
c1 = [[0 for _ in range(c)] for _ in range(3)]
for i in range(n):
    for j in range(n):
        if (i + j) % 3 == 0:
            c0[0][s[i][j] - 1] += 1
        elif (i + j) % 3 == 1:
            c0[1][s[i][j] - 1] += 1
        elif (i + j) % 3 == 2:
            c0[2][s[i][j] - 1] += 1
for i in range(3):
    for j in range(c):
        for k in range(c):
            c1[i][j] += d[k][j] * c0[i][k]
"""
c2, c3 = [], []
for i in range(3):
    c2 = []
    for j in range(3):
        x = c1[i]
        a = [min(x), x.index(min(x))]
        c2.append(a)
        c1[i][c1[i].index(min(c1[i]))] = 10 ** 9
    c3.append(c2)
ans = 10 ** 9
for i in range(3):
    for j in range(3):
        for k in range(3):
            if c3[0][i][1] != c3[1][j][1] and c3[0][i][1] != c3[2][k][1] and c3[2][j][1] != c3[2][k][1]:
                m = c3[0][i][0] + c3[1][j][0] + c3[2][k][0]
                if m < ans:
                    ans = m
print(ans)"""
m = 0
ans = 10 ** 9
for i in range(c):
    for j in range(c):
        for k in range(c):
            if i != j and j != k and k != i:
                m = c1[0][i] + c1[1][j] + c1[2][k]
                if m < ans:
                    ans = m
print(ans)