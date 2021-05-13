def beginner():
    # 入力
    N, R = map(int, input().split())
    # 処理
    if N >= 10:
        return R
    else:
        return R + 100 * (10 - N)

result = beginner()
print(result)