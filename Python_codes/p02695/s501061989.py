import itertools

N, M, Q = map(int, input().split())
ABCD = [list(map(int, input().split())) for _ in range(Q)]

# 1 ~ Mまでの数を用いたN項の重複組合せを作成する
arrs = []
for arr in itertools.combinations_with_replacement(range(1, M + 1), N):
    arrs.append(list(arr))
#print(len(arrs))

# 各組合せに対し、全クエリを実行して最大値を求める　(計算量: 10H10 x 50)
answer = - float("inf")
for arr in arrs:
    tmp = 0
    for a, b, c, d in ABCD:
        if arr[b - 1] - arr[a - 1] == c:
            tmp += d
    answer = max(answer, tmp)

print(answer)