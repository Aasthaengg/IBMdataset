from collections import defaultdict

n = int(input())
M = []
for i in range(n):
    x, y = map(int, input().split())
    M.append([x, y])
M.sort(key=lambda x: (x[0], x[1]))
X = defaultdict(int)
for i in range(n - 1):
    for j in range(i + 1, n):
        a = M[i][0] - M[j][0]
        b = M[i][1] - M[j][1]
        X[(a, b)] += 1
print(n - max(X.values(), default=0))