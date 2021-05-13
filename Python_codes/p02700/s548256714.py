# abc164B
# https://atcoder.jp/contests/abc164/tasks/abc164_b

# 高橋君モンスターの体力はA、攻撃力はB
# 青木君モンスターの体力はC、攻撃力はD

# 高橋君が勝ったら"Yes"、負けたら"No"

# 入力
a, b, c, d = map(int, input().split())

# 処理
# 必殺技を受けた残りの体力
while a > 0 and c > 0:
    a -= d
    c -= b

if c <= 0:
    print("Yes")
else:
    print("No")

