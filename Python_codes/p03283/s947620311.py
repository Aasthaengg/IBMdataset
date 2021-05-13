n, m, q = map(int, input().split())
lst = [[0 for j in range(n)] for i in range(n+1)]
for i in range(m):
    li, ri = map(int, input().split())
    ri -= 1
    lst[li][ri] += 1
query = []
for i in range(q):
    pi, qi = map(int, input().split())
    pi -= 1; qi -= 1
    query.append([pi, qi])

for i in range(n):
    for j in range(n):
        lst[i+1][j] += lst[i][j]

for pi, qi in query:
    ans = 0
    for i in range(pi, qi+1):
        ans += lst[qi+1][i] - lst[pi][i]
    print(ans)