D, G = map(int, input().split())
p_list = [list(map(int, input().split())) for i in range(D)]

# 基本的に配点の高い問題を解いていく方が効率が良いはず
# ビット全探索、D行目の問題を全部解く場合を1, そうでないものを0とする。
ans = 10**18
from itertools import product

for bit in product((0,1), repeat=D):
    point = 0
    mondai = 0
    # (0,0) (0,1)などのビット列を生成
    for i in range(D):
        point += bit[i]*p_list[i][0]*100*(i+1)
        if bit[i] == 1:
            mondai +=p_list[i][0]
            point += p_list[i][1]
    # G-point > 0ならば、配点の高い問題を順に解いていってその時の問題数をカウントする
    if G - point > 0:
        # 最後に0となっているbitを取得
        a = [i for i, x in enumerate(bit) if x == 0]
        lastbit = int(a[-1])
        for j in range(p_list[lastbit][0]):
            point += (lastbit+1) * 100
            mondai += 1
            if (G - point <= 0):
                ans = min(ans, mondai)
                break
        # まだ G - pointが正ならば解なしで次のビット探索へ
        if G - point > 0:
            mondai = 10 ** 18

    ans = min(ans, mondai)

print(ans)

