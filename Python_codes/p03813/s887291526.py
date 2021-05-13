# A - ABC/ARC
#
# 現在のレートが 1200 未満ならば AtCoder Beginner Contest (ABC) に、
# そうでなければ AtCoder Regular Contest (ARC) に参加

# 現在のレート x が与えられる。

# 参加するコンテストが ABC ならば ABC
# そうでなければ、 ARC と出力

# x を標準入力から得る
x = int(input())
# print(x)

# x が 1200 未満なら ABC
# そうでなければ ARC
if x < 1200:
    answer = "ABC"
else:
    answer = "ARC"

# 結果を出力
print(answer)
