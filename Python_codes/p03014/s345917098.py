h, w = map(int,input().split())
s = [list(input()) for i in range(h)]

#障害物がない直線経路を前計算しておく
L = [[0] * w for i in range(h)]
R = [[0] * w for i in range(h)]
U = [[0] * w for i in range(h)]
D = [[0] * w for i in range(h)]

for i in range(h):
    for j in range(w):
        temp_L = s[i][j]
        temp_R = s[i][-(j + 1)]
        temp_U = s[i][j]
        temp_D = s[-(i + 1)][j]

        if temp_L == '#':L[i][j] = 0
        else:
            if j == 0:L[i][j] = 1
            else:L[i][j] = L[i][j - 1] + 1

        if temp_R == '#':R[i][-(j + 1)] = 0
        else:
            if j == 0:R[i][-(j + 1)] = 1
            else:R[i][-(j + 1)] = R[i][-(j + 1) + 1] + 1

        if temp_U == '#':U[i][j] = 0
        else:
            if i == 0:U[i][j] = 1
            else:U[i][j] = U[i - 1][j] + 1

        if temp_D == '#':D[-(i + 1)][j] = 0
        else:
            if i == 0:D[-(i + 1)][j] = 1
            else:D[-(i + 1)][j] = D[-(i + 1) + 1][j] + 1

ans = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':continue
        temp = L[i][j] + R[i][j] + U[i][j] + D[i][j] - 3
        if ans < temp:ans = temp
print(ans)
#print(L,R,U,D,sep ='\n')