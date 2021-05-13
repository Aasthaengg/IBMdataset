# 問題文
# アライグマはモンスターと戦っています。モンスターの体力は Hです。
# アライグマはN種類の必殺技を使うことができ、i番目の必殺技を使うとモンスターの体力を Ai減らすことができます。
# 必殺技を使う以外の方法でモンスターの体力を減らすことはできません。
# モンスターの体力を0以下にすればアライグマの勝ちです。
# アライグマが同じ必殺技を 2度以上使うことなくモンスターに勝つことができるなら Yes を、できないなら No を出力してください。

# H（体力）,N（種類）：標準入力
# リストの中のA(体力を減らす：攻撃力)：リストを作成し、標準入力
h, n = map(int, input().split())
A = list(map(int, input(). split()))


# 攻撃力Aが0からNの間で増えていくとき、
# H が 0 以下のとき Yes、そうでないとき No となる。

def hp(h: int, n: int, A: list) -> str:
    damage = 0                   # ダメージは最初0なので、0と定義
    for i in range(0, n):        # 0からn番目まで繰り返す時
        damage += int(A[i])      # リスト[i]（インデックスi番目）をintに変更
        i += 1                   # 0番目からi番目まで1ずつ足されていく

    if (h - damage) <= 0:     # forの中で、残った体力が0以下であれば倒せる→Yes
        return 'Yes'
    else:              # 残った体力が0以上の時は倒せる→No
        return 'No'


print(hp(h, n, A))

# TypeError: list expected at most 1 argument, got 2