def papers_please():
    # 入力
    N = int(input())
    A = list(map(int, input().split()))
    # 処理
    for one_num in A:
        # 偶数
        if one_num % 2 == 0:
            # 3 or 5 で割り切れる
            if one_num % 3 == 0 or one_num % 5 == 0:
                pass
            # 割り切れない
            else:
                return 'DENIED'
        # 奇数
        else:
            pass
    # 3 or 5 で割り切れない偶数がない場合
    return 'APPROVED'

result = papers_please()
print(result)