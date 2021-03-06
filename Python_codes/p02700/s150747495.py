# 高橋君と青木君がモンスターを闘わせます。
# 高橋君のモンスターは体力が Aで攻撃力が Bです。 青木君のモンスターは体力が Cで攻撃力が Dです。
# 高橋君→青木君→高橋君→青木君→... の順に攻撃を行います。 攻撃とは、相手のモンスターの体力の値を自分のモンスターの攻撃力のぶんだけ減らすことをいいます。
# このことをどちらかのモンスターの体力が 0以下になるまで続けたとき、 先に自分のモンスターの体力が 0以下になった方の負け、そうでない方の勝ちです。
# 高橋君が勝つなら Yes、負けるなら No を出力してください。

A, B, C, D = map(int, input().split())

while A or C > 0:
    aoki_hitpoint = C - B
    if aoki_hitpoint <= 0:
        C = 0
        print("Yes")
        exit()
    else:
        C = aoki_hitpoint

    takahashi_hitpoint = A - D
    if takahashi_hitpoint <= 0:
        print("No")
        A = 0
        exit()
    else:
        A = takahashi_hitpoint