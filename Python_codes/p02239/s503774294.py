n = int(raw_input())
G = [[0 for i in range(n+1)] for j in range(n+1)]
d = [-1 for i in range(n+1)]

for i in range(n):
    v = map(int, raw_input().split())
    for j in range(v[1]):
        G[v[0]][v[2+j]] = 1

flag = [0 for i in range(n+1)]
tn = [[0 for i in range(n+1)] for j in range(n+1)]
tn[0][1] = 1
r = 0
for i in range(n):
    for j in range(1, n+1):
        if flag[j] == 0 and tn[i][j] == 1:
            flag[j] = 1
            d[j] = r
            for k in range(1, n+1):
                if G[j][k] == 1:
                    tn[i+1][k] = 1
    r += 1

for i in range(1, n+1):
    print(str(i) + " " + str(d[i]))