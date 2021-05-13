#164b
#1.値を受け取る
A, B, C, D = map(int, input().split())

#2.結果を出力する
while C or A >= 0:
    C =C - B
    A =A - D
    if C <= 0:
        print('Yes')
        break
    if A <= 0:
        print('No')
        break