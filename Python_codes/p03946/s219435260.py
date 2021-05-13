N, T = map(int, input().split())
A = list(map(int, input().split()))
Max = [0] * N
revenue = 0
for i in range(N)[::-1]:
    if i == N-1:
        Max[i] = (A[i], 1)
        continue
    ma, cnt = Max[i+1]
    if ma > A[i]:
        Max[i] = Max[i+1]
    elif ma == A[i]:
        Max[i] = (ma, cnt + 1)
    else:
        Max[i] = (A[i], 1)
    revenue = max(revenue, Max[i][0] - A[i])

D = dict()

for a, (m, c) in zip(A, Max):
    if m - a == revenue:
        if (m, a) in D:
            x, y = D[(m, a)]
            D[(m, a)] = (x + 1, max(y, c))
        else:
            D[(m, a)] = (1, c)

ans = 0
for key, value in D.items():
    x, y = value
    ans += min(x, y)
print(ans)
