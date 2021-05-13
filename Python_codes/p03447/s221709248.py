# 各金額を取得
X = int(input())
A = int(input())
B = int(input())

# 残金を計算
# 1.ケーキ1つの購入
Balance = X - A
# 2.残金で購入可能な最大個数のドーナツを購入
Balance = Balance - (Balance // B) * B

# 残金の出力
print(Balance)