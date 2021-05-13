n = int(input())

TABLES = []
H = []
for _ in range(n):
    x, y, h = map(int, input().split())
    TABLE = [[0] * 101 for _ in range(101)]
    for i in range(101):
        for j in range(101):
            TABLE[i][j] = h + abs(x - i) + abs(y - j)
    TABLES.append(TABLE)
    H.append(h)

for k in range(n):
    if H[k] != 0:
        a = k
        break

for i in range(101):
    for j in range(101):
        temp = TABLES[a][i][j]
        flag = True
        for k in range(n):
            if H[k] == 0:
                if TABLES[k][i][j] < temp:
                    flag = False
                    break
            else:
                if TABLES[k][i][j] != temp:
                    flag = False
                    break
        if flag:
            print(i, j, temp)
            exit()
