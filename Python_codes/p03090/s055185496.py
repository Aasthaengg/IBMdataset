N = int(input())

# 完全グラフは惜しい
# 各頂点から自身を除く頂点すべてに辺を貼る
# 誤差をなくすために辺を削る
# 元々十分に辺が張られているので、連結は保たれるだろう

# 補グラフ

# 要素数の偶奇で異なる
# 奇数: [1-6, 2-5, 3-4, 7]
# 偶数: [1-8, 2-7, 3-6, 4-5]

e = [[False for _ in range(N + 1)] for _ in range(N + 1)]
# 1-indexed
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j: continue
        e[i][j] = True
        e[j][i] = True
# 完全グラフを作る

total = -1
if N % 2 == 0:
    total = N + 1
else:
    total = N
# 補グラフのcounterpartを探すのに使用
# total - 自身 = 相方

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j: continue
        cp_i = total - i
        e[i][cp_i] = False
        # 辺を削る

print(sum(e[i].count(True) for i in range(1, N + 1)) // 2)
# 辺をa->b, b->aで二重計上しているので、半分にする

for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        if e[i][j]:
            print(i, j)
