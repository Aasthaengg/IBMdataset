# 入力 : 数字3つ、別々に
X = int(input())
A = int(input())
B = int(input())

# 出力
afterA = X - A
numofB = int(afterA / B)
Ans = afterA - B * numofB
print(Ans)
