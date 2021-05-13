# -*- coding: utf-8 -*-

# 入力から変数を初期化
N, H = map(int, input().split())
a = []
b = []
for i in range(N):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
ans = H

# 振る刀の最大値
amax = max(a)

# 投げる刀を降順でソートしておく
b.sort(reverse=True)

# 攻撃力の高い刀から順にk本投げ、残りの体力をamaxを使って削る
damage_throw = 0
for k in range(N+1):
    damage_throw += 0 if k == 0 else b[k-1]
    H_minus_throw = H - damage_throw
    if H_minus_throw <= 0:
        tmp_ans = k
    else:
        num_swing = -(-H_minus_throw // amax)
        tmp_ans = k + num_swing
    ans = min(tmp_ans, ans)

print(ans)
