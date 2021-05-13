import itertools

N = int(input())
# [[1番の人の証言], [2番の人の証言], ..., [N番の人の証言]]
l = [[-1 for _ in range(N)] for _ in range(N)]
# N人についてそれぞれ証言をまとめる
for i in range(N):
    # 証言の数
    a = int(input())
    # 各証言をlに格納
    for _ in range(a):
        x, y = map(int, input().split())
        l[i][x - 1] = y

ans = 0

# 全通りを列挙
perm = list(itertools.product([0, 1], repeat=N))
# それぞれの選び方について
for p in perm:
    flag = True
    # pの中身を左から順に見ていく
    for j in range(N):
        # 既に破綻していたら、以降は証言をチェックする必要はない
        if flag == False:
            break
        # jの全員に対する証言について
        for k in range(N):
            # 狂人(p[j]==0)の証言は意味がないので無視して良い
            if p[j] == 1:
                # l[j][k] == -1 なら、その人に対する証言は存在しない
                # kについての証言と、kの実情が異なる場合（矛盾）
                if l[j][k] != -1 and l[j][k] != p[k]:
                    flag = False
                    break

    # 一つも矛盾が存在しなかった場合
    # sum(d)は聖人の総数を表す
    if flag == True:
        ans = max(ans, sum(p))

print(ans)
