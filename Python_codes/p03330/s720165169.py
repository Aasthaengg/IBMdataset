# D - Good Grid

N, C =  map(int, input().split())
D = [list(map(int, input().split())) for _ in range(C)]
c = [list(map(int, input().split())) for _ in range(N)]

group0, group1, group2 = [0]*C, [0]*C, [0]*C
for row in range(N):
    for col in range(N):
        if (row + col) % 3 == 0:
            group0[c[row][col] -1] += 1
        elif (row + col) % 3 == 1:
            group1[c[row][col] -1] += 1
        else:
            group2[c[row][col] -1] += 1

ans = []
for color0 in range(C):
    for color1 in range(C):
        for color2 in range(C):
            if len(set([color0, color1, color2])) == 3:
                tmp = 0
                for idx in range(C):
                    tmp += D[idx][color0] * group0[idx]
                    tmp += D[idx][color1] * group1[idx]
                    tmp += D[idx][color2] * group2[idx]
                ans.append(tmp)

print(min(ans))