# 入力 : A B C D
A, B, C, D = map(int, input().split())

# 出力　大きい方の面積
area1 = A * B
area2 = C * D

print(max(area1, area2))
