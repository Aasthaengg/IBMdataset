# Grid Coloring

h, w = map(int, input().split())
n = int(input())
a = [int(_) for _ in input().split()]

# 開始座標
x, y = 0, 0
# x座標に関するステータス
# 0のとき0→(w-1), 1のとき(w-1)→0
status = 0

# 答え入れる配列
ans = [[0] * w for _ in range(h)]

for i in range(n):
    for j in range(a[i]):
        #print(x, y, i, j)
        ans[y][x] = i+1
        if status == 0:
            x += 1
        else:
            x -= 1
        if x == w:
            status = 1
            x -= 1
            y += 1
        if x == -1:
            status = 0
            x += 1
            y += 1

for i in ans:
    for j in i:
        print(j, end=' ')
    print()