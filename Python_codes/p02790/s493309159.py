def comparing_strings():
    # 入力
    a, b = input().split()
    # 初期処理
    str_a = ''
    str_b = ''
    # 文字列作成
    for _ in range(int(b)):
        str_a = str_a + a
    for _ in range(int(a)):
        str_b = str_b + b
    # 大小比較
    if str_a <= str_b:
        return str_a
    else:
        return str_b

result = comparing_strings()
print(result)