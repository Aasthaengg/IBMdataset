#086a

a, b = map(int, input().split())  # スペースで区切った二つの整数を取得する記載

ab = a * b  # a,bの積を代入

surplus = ab % 2    # 2で割ったあまりを代入

if surplus == 1: # 余りが1なら奇数
    print('Odd')
else:   # 余りが1以外（0)なら偶数
    print('Even')

