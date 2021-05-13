N, M = [int(x) for x in input().split()]
A = set()

MOD = 10 ** 9 + 7

for _ in range(M):
    A.add(int(input()))

result = {0: 1}

for i in range(1, N+1):

    # 階段が壊れている場合にはそこに行くパターンは無い
    if i in A:
        result[i] = 0

    # それ以外の場合、前の段と前の前の段まで行くパターンを加算した数になる
    else:
        if i - 1 in result:
            min_1 = result[i-1]
        else:
            min_1 = 0
        if i - 2 in result:
            min_2 = result[i-2]
        else:
            min_2 = 0
        result[i] = (min_2 + min_1) % MOD

print(result[N])
