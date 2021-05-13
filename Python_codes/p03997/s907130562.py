# 上底の長さが a、下底の長さが b、高さが hの台形があります。
# この台形の面積を求めてください。

# 制約
# 1 ≦ a ≦ 100
# 1 ≦ b ≦ 100
# 1 ≦ h ≦ 100
# 入力で与えられる値はすべて整数
# hは偶数

# 標準入力から a, b, h の値を取得する。
input_a = int(input())
input_b = int(input())
input_h = int(input())

# 台形の計算をし、結果を出力する
result = int((input_a + input_b) * input_h / 2)
print(result)
