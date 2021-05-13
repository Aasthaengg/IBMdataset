# https://atcoder.jp/contests/abc106/tasks/abc106_d

# MAX_N = 505
n, m, q = map(int, input().split())
X = [[0] * (n + 1) for _ in range(n + 1)]
C = [[0] * (n + 1) for _ in range(n + 1)]
count = [0] * (n + 1)
for _ in range(m):
    li, ri = map(int, input().split())
    X[li][ri] += 1
for i in range(1, n + 1):
    for j in range(1, n + 1):
        C[i][j] = C[i][j - 1] + X[i][j]

for _ in range(q):
    p, q = map(int, input().split())
    sum_k = 0
    for j in range(p, q + 1):
        sum_k += C[j][q] - C[j][p - 1]
    print(sum_k)