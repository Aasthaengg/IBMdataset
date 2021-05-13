r, c = map(int, input().split())
sheet = [[int(n) for n in input().split()] for i in range(r)]
sheet_sum = [[0 for i in range(c + 1)] for j in range(r + 1)]
for i in range(r):
    for j in range(c):
        sheet_sum[i][j] = sheet[i][j]
    sheet_sum[i][c] = sum(sheet[i])
for i in range(c + 1):
    for j in range(r):
        sheet_sum[r][i] += sheet_sum[j][i]
for i in range(r + 1):
    for j in range(c + 1):
        if j == c:
            print(sheet_sum[i][j])
        else:
            print(sheet_sum[i][j], end = " ")