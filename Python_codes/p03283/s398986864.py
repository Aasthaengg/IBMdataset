# https://atcoder.jp/contests/abc106/tasks/abc106_d

'''
N が小さいので、N^2 を考えると良いことが分かる。
'''

from collections import defaultdict

N, M, Q = map(int, input().split())        # N, M: リストの長さ

edges = [list(map(int, input().split())) for _ in range(M)]

data = defaultdict(int)                  # defaultdict は 初期化の際のに value の type を指定する必要あり

for i, j in edges:
    i -= 1
    j -= 1
    data[(i,j)] += 1

cum = [[0]*(N+1) for _ in range(N+1)]

for i in range(N):
    for j in range(N):
        cum[i+1][j+1] = cum[i][j+1] + cum[i+1][j] - cum[i][j] + data[(i,j)]

for _ in range(Q):
    p, q = map(int, input().split())
    if p < q:
        p, q = q, p
    q -= 1
    res = cum[p][p] - cum[p][q] - cum[q][p] + cum[q][q]
    print(res)





