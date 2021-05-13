# コードを取得
S = str(input())

# リストに分割をして隣接する数値を比較
c_list = list(S)
cnt = 1
judge = "Good"
for cnt in range(1,4,1):
    if c_list[cnt-1] == c_list[cnt]:
        judge = "Bad"

# 結果を出力
print(judge)