# aは整数 , sは文字列　標準入力
a = int(input())
s = str.lower(input())


if 3200 <= a < 5000:
    if len(s) < 11:
        print(s)
elif 2800<= a < 3200:
    print("red")