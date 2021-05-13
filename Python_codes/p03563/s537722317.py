# 入力 : 数字2つ、別々に
R = int(input())
G = int(input())

# 出力 : RをGに上げるためにとるためのX
X = R + (G-R) * 2
print(X)
