# 高橋くんのモンスター　体力A 攻撃B
# 青木くんのモンスター　体力C 攻撃D
# それぞれの値の入力
A, B, C, D = map(int, input().split())

#　高橋君→青木君→...で攻撃
# 攻撃は相手の体力の値を自分のモンスターの攻撃力分だけ減らす。
while True:
    C -= B
    A -= D

    # 高橋君が勝つ場合
    if C <= 0:
        result = 'Yes'
        break
    #　青木君が勝場合
    if A <= 0:
        result = 'No'
        break

print(result)