# コンテスト名の要求
S = input()

# 入力されたコンテストではないものを出力
if S == "ABC":
    print("ARC")
elif S == "ARC":
    print("ABC")
else:
    print("入力内容が正しくありません。")