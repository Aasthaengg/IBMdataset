def distinct_or_not():
    # 入力
    N = int(input())
    A = list(map(int, input().split()))
    # Aを集合型に変換
    A_set = set(A)
    # AとA_setを比較
    if len(A) == len(A_set):
        return 'YES'
    else:
        return 'NO'

result = distinct_or_not()
print(result)