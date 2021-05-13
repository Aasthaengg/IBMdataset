# 標準出力を取得（strデータ）
# A タップの口数　B 必要な口数
A, B = input().split()

# A, B を integerに変換
A = int(A)
B = int(B)

# OAタップの数を表す変数の初期値を 1 とする
num = 1

# B(必要な口数) が 1 の時はタップは必要ない
if B == 1:
    num = 0
else:
    while (A - 1) * (num - 1) + A < B:
        num = num + 1

# 結果を出力
print(num)