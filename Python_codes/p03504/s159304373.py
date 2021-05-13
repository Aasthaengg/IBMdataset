n, c = map(int, input().split())
r = [[0 for i in range(c)] for j in range(100000)]  # テレビ局の番組表
for dummy in range(n):  # 入力
    s, t, c = map(int, input().split())
    for j in range(s - 1, t):
        r[j][c - 1] = 1  # 放送中なら1
ans = 0
for i in range(100000):
    if sum(r[i]) > ans:
        ans = sum(r[i])  # 同時に放送されている番組の最大数
print(ans)