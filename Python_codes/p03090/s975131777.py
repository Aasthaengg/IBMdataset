n = int(input())

pairs = [[i for i in range(1, n + 1)] for _ in range(n)]

ans = []
if n % 2 == 0:
    for i in range(n-1):
        for j in range(i + 1, n):
            x = pairs[i][j]
            if x == n - i:
                continue
            ans.append((i + 1, x))
else:
    for i in range(n-1):
        for j in range(i + 1, n):
            x = pairs[i][j]
            if x == n - i-1:
                continue
            ans.append((i + 1, x))

print(len(ans))
for x, y in ans:
    print(x, y)
