# 入力
X = int(input())# 所持金
A = int(input())# ケーキの値段
B = int(input())# ドーナツの値段

# 処理
balance = X - A
donut_count = balance // B
total_balance = balance - donut_count * B

# 出力
print(total_balance)