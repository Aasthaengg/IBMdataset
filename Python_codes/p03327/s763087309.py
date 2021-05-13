# 099A
# N回目のコンテスト
# 999回まで ABC、1000回目から1998回目 ABD

# 入力
n = int(input())

# 処理
if n < 1000:
    print("ABC")
elif n >= 1000:
    print("ABD")
