import itertools


def actual(n, D):
    comb = itertools.combinations(D, 2)

    # return sum([x * y for x, y in comb])

    """
    「順番を考慮しない2要素の選び方」を全探索する際のポイント
        内側のループ変数の始点を外側のループ変数 +1 から始めるとよい。
        これにより、内側のループで選ぶインデックスが必ず外側のループで選ぶインデックスより大きくなり、
        同じ選び方を 2 回見てしまうことを回避できます。"""
    s = 0
    for i in range(len(D)):
        for j in range(i + 1, len(D)):
            s += D[i] * D[j]

    return s

n = int(input())
D = list(map(int, input().split()))

print(actual(n, D))