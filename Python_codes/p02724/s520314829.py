X = int(input())

# 500円硬貨 1枚につき 1000、5円硬貨 1枚につき 5 の 嬉しさ を得ます。
# X円を持っています。嬉しさの最大値を出力せよ。

s = X // 500
a = X % 500
t = a // 5
print(s*1000 + t*5)