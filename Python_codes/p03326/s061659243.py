n, m = map(int, input().split())
cakes = [list(map(int, input().split())) for _ in range(n)]

each_r = [[0] * n for _ in range(8)]

for i in range(n):
    each_r[0][i] =  cakes[i][0] + cakes[i][1] + cakes[i][2]
    each_r[1][i] =  cakes[i][0] + cakes[i][1] - cakes[i][2]
    each_r[2][i] =  cakes[i][0] - cakes[i][1] + cakes[i][2]
    each_r[3][i] =  cakes[i][0] - cakes[i][1] - cakes[i][2]
    each_r[4][i] = -cakes[i][0] + cakes[i][1] + cakes[i][2]
    each_r[5][i] = -cakes[i][0] + cakes[i][1] - cakes[i][2]
    each_r[6][i] = -cakes[i][0] - cakes[i][1] + cakes[i][2]
    each_r[7][i] = -cakes[i][0] - cakes[i][1] - cakes[i][2]

results = [0] * 8
for i in range(8):
    each_r[i].sort(reverse=True)
    results[i] = sum(each_r[i][0:m])
print(max(results))
