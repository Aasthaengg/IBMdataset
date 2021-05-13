# 正の整数aとb
a, b = map(int, input().split())
# aとbの積が偶数か奇数か判別する

# 積が奇数なら'Odd'、偶数なら'Even'と出力する
if int(a * b / 2) < int(a * b / 2 + 0.5):
    print('Odd')
else:
    print('Even')