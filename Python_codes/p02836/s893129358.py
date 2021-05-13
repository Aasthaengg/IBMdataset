def palindrome_philia():
    # 入力
    S = input()
    # 処理
    # 文字列が奇数
    if len(S) % 2 == 1:
        comp_str_count = int((len(S) + 1) / 2 - 1)
    # 文字列が偶数
    elif len(S) % 2 == 0:
        comp_str_count = int((len(S) + 1) / 2)
    # 集計処理
    hag_count = 0
    for i in range(comp_str_count):
        if S[i] == S[-i-1]:
            pass
        else:
            hag_count += 1
        i += 1
    return hag_count

result = palindrome_philia()
print(result)