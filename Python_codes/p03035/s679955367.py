i = list(map(int, input().split())) #i_1 i_2を取得し、iに値を入れる
A = i[0] #出力：i_1
B = i[1] #出力：i_2

if A >= 13:
    print(B)
elif A >= 6:
    print(int(B/2))
else:
    print(0)