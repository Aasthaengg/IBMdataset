# AtCoder 社は、毎週土曜日にコンテストを開催しています。
# コンテストには ABC と ARC の 2つの種類があり、
# 毎週どちらか一方が開催されます。
# ABC が開催された次の週には ARC が開催され、
# ARC が行われた次の週には ABC が開催されます。
# 先週開催されたコンテストを表す文字列 S が与えられるので、
# 今週開催されるコンテストを表す文字列を出力してください。

# 制約
# Sは'ABC' または'ARC'

# 標準入力から文字列 S を取得する
s = input()

# S をたよりに、今週開催されるコンテストを出力する
next_contest = "ret"
if s == "ABC":
    next_contest = "ARC"
elif s == "ARC":
    next_contest = "ABC"

print(next_contest)
