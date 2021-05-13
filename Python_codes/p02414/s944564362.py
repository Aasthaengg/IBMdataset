m, n, k = map(int, input().split())
A, B = [], []
for _ in range(m):
    A.append(list(map(int, input().split())))
for _ in range(n):
    B.append(list(map(int, input().split())))

for index, row in enumerate(A):
    ans = []
    for i in range(k):
        col = [rowB[i] for rowB in B]
        ans.append(sum([x * y for x, y in zip(row, col)]))
    print(' '.join(map(str, ans)))
