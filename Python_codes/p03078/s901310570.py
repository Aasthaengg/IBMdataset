from heapq import heappop, heappush

X, Y, Z, K = map(int, input().split())

# heahqで最大値を扱いたいのでマイナスにしておく
A = sorted(list(map(lambda x: -int(x), input().split())))
B = sorted(list(map(lambda x: -int(x), input().split())))
C = sorted(list(map(lambda x: -int(x), input().split())))

#　プライオリティキュー
#　heapqの要素はタプルに出来る
hq = []
u = (A[0] + B[0] + C[0], 0, 0, 0)
heappush(hq, u)

# 同じものを複数回追加しないようにチェック
visited = set()
visited.add(u)

for i in range(K):
    x, i, j, k = heappop(hq)
    print(-x)
    # A, B, Cについての次の値をpush
    if i + 1 <= X - 1:
        next_i = (A[i + 1] + B[j] + C[k], i + 1, j, k)
        if next_i not in visited:
            heappush(hq, next_i)
            visited.add(next_i)
    if j + 1 <= Y - 1:
        next_j = (A[i] + B[j + 1] + C[k], i, j + 1, k)
        if next_j not in visited:
            heappush(hq, next_j)
            visited.add(next_j)
    if k + 1 <= Z - 1:
        next_k = (A[i] + B[j] + C[k + 1], i, j, k + 1)
        if next_k not in visited:
            heappush(hq, next_k)
            visited.add(next_k)
