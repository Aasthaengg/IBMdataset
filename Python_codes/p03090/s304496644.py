"""
・偶奇に分けて考える
・完全グラフと正解のグラフを比較する
・「任意の頂点」と「その頂点から削除する辺」の関係を考える

偶数
-> 和が(N+1)となる頂点を繋いでいない
奇数
-> 頂点Nからは全て引く。
-> それ以外は、和がNとなる頂点を繋いでいない。
"""

N = int(input())

M = 0
ans = []

# 1 <= i < j <= N

if N % 2 == 0:
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            if i + j != N + 1:
                ans.append((i, j))
                M += 1
else:
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            if i + j != N:
                ans.append((i, j))
                M += 1

print(M)
for i, j in ans:
    print(i, j)