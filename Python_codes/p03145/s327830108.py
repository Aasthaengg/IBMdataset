#116A
# 1.値を正しく取得
a, b, c = (int(x) for x in input().split())

# 2.正しく処理
menseki = a * b / 2

print(int(menseki))