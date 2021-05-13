import bisect

n, d, a = map(int, input().split())
XB = []
X = []
for _ in range(n):
    x, h = map(int, input().split())
    bomb = int(-(-h//a))
    XB.append([x, bomb])
    X.append(x)

XB = sorted(XB, key=lambda x:x[0])
X = sorted(X)

# x1+dがx2-d以上のときに、まとめてダメージを与えられる
# x2がダメージを受けうる、x1を二分探索する

X_range = [[-1]]

for i in range(1,n):
    now = X[i]
    # X[x_ind]以上の爆弾ダメージをX[i]は受ける
    x_ind = bisect.bisect_left(X, X[i]-2*d)
    if x_ind == i:
        X_range.append([-1])
    else:
        X_range.append([x_ind, i-1])

# print(X)

# 各箇所で何回爆弾を使用したのかを保持 -> 累積しておく
# X[i]を見るときに、X[i-1]~X[ind]間で使用した爆弾の個数を求める
# 足りない文はX[i]で爆発させる

Bomb = [XB[0][1]]
Bomb_rui = [0, XB[0][1]]

for i in range(1,n):
    need_bomb = XB[i][1]
    if X_range[i][0] == -1:
        Bomb.append(need_bomb)
        Bomb_rui.append(Bomb_rui[-1]+need_bomb)
    else:
        before_bomb = Bomb_rui[X_range[i][1]+1] - Bomb_rui[X_range[i][0]]
        if before_bomb >= need_bomb:
            Bomb.append(0)
            Bomb_rui.append(Bomb_rui[-1])
        else:
            need_bomb -= before_bomb
            Bomb.append(need_bomb)
            Bomb_rui.append(Bomb_rui[-1]+need_bomb)

ans = Bomb_rui[-1]
# print(Bomb)
# print(Bomb_rui)
# print(X_range)
print(ans)