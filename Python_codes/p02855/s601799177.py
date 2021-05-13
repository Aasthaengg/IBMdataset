

H,W,K = map(int, input().split())

S = [input() for _ in range(H)]
ans = [[0 for _ in range(W)] for _ in range(H)]

# 左上から見ていった時に見つかったイチゴの個数
cnt_sb = 0
for i in range(H):
    # その行で見つかったイチゴの数
    cnt_sb_row = 0
    for j in range(W):
        # あるマスでいちごが　見つかった時
        if S[i][j] == "#":
            cnt_sb += 1
            cnt_sb_row += 1
        # ピースの番号。その行でイチゴが見つかっていない場合は今までに見つかったイチゴの数+1。（直前の行と被らないようにするため）
        # その行でイチゴが見つかっていれば、現時点で見つかったイチゴの数
        if cnt_sb_row == 0:
            ans[i][j] = cnt_sb + 1
        else:
            ans[i][j] = cnt_sb


    # ある行にイチゴがなかった場合は、上にあるピースに所属するよう修正する
    if cnt_sb_row == 0:
        # イチゴが一つでも見つかっている状態なら、丸っと一行同じにできる
        if cnt_sb != 0:
            ans[i] = ans[i-1]
        
    # 上から調べたときに、i行目で初めてイチゴが見つかった場合、
    # その時点では、iより上は全部同じピース扱いになっているので、i行目と同じように切り分ける
    if cnt_sb != 0 and cnt_sb == cnt_sb_row:
        for j in range(i):
            ans[j] = ans[i]

for i in range(H):
    print(*ans[i])