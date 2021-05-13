def minor_change():
    # 入力
    S = input()
    T = input()
    # 比較処理
    char_count = len(S)
    replace_count = 0
    for i in range(char_count):
        if S[i] != T[i]:
            replace_count += 1
    return replace_count

result = minor_change()
print(result)