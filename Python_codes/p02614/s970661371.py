from sys import stdin
import itertools

H, W, K = map(int, input().split())
table = []

all = 0  # 黒の総計
row = [0] * H  # 各行の黒の数
column = [0] * W  # 各列の黒の数

for i in range(H):
    h_i = list(stdin.readline()[:-1])
    table.append(h_i)
    row[i] = h_i.count("#")
    all += row[i]

for j in range(W):
    for i in range(H):
        column[j] += table[i][j] == "#"

# print(row)
# print(column)

ans = 0
for x in range(H):  # 赤く塗る行の数
    for rs in itertools.combinations(range(H), x):  # 赤く塗る行の組み合わせ
        for y in range(W):  # 赤く塗る列の数
            for cs in itertools.combinations(range(W), y):  # 赤く塗る列の組み合わせ
                # print(f"row: {list(rs)}, colums: {list(cs)}", end=" ")
                painted = 0  # 塗られた黒の数
                for i in rs:
                    painted += row[i]
                for j in cs:
                    painted += column[j]
                for i in rs:
                    for j in cs:
                        painted -= table[i][j] == "#"  # 行と列の分を引き、重なったところが黒なら二重で引かないようにする
                if all - painted == K:
                    ans += 1

print(ans)
