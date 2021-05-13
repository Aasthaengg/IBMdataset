# 入力
S = str(input())

# 処理
if S[0] == S[1] or S[1] == S[2] or S[2] == S[3]:
    result = "Bad"
else:
    result = "Good"

# 出力
print(result)