# 大会の回数を取得
N = int(input())

if N < 1000:
    Contest = "ABC"
    print(Contest)
elif N >= 1000:
    Contest = "ABD"
    print(Contest)