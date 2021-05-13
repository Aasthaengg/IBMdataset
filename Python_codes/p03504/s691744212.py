N, C = map(int, input().split())
MAX_N = (10 ** 5 + 5)
X = [[0] * MAX_N for _ in range(C)]

for _ in range(N):
    s, t, c = map(int, input().split())
    c -= 1
    X[c][s] += 1
    X[c][t + 1] -= 1
# print(X)
res = [[0] * MAX_N for _ in range(C)]
for c in range(C):
    for i in range(MAX_N - 1):
        res[c][i + 1] = res[c][i] + X[c][i]
# print(ans)
ans = 0
for i in range(MAX_N - 1):
    count = 0
    for c in range(C):
        if 0 < res[c][i]:
            count += 1
    ans = max(ans, count)
print(ans)
