import itertools

N, M, Q = map(int, input().split())
abcd = [list(map(int, input().split())) for i in range(Q)]

# (1,2,...,M)からN個選ぶ重複組み合わせを生成
# ex. N=3, M=4
# [(1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 1, 4), (1, 2, 2), (1, 2, 3), (1, 2, 4), (1, 3, 3), (1, 3, 4), (1, 4, 4),
# (2, 2, 2), (2, 2, 3), (2, 2, 4), (2, 3, 3), (2, 3, 4), (2, 4, 4), (3, 3, 3), (3, 3, 4), (3, 4, 4), (4, 4, 4)]

# (1,2,...,M)のリスト
l = range(1, M + 1)
nCr = list(itertools.combinations_with_replacement(l, N))
# print(nCr)

# 最終的な答え
ans = 0
for A in nCr:
    # 各組み合わせで得られる点数
    tmp = 0
    for a, b, c, d in abcd:
        if A[b - 1] - A[a - 1] == c:
            tmp += d
    ans = max(ans, tmp)

print(ans)
