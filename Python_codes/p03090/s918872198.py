n = int(input())
x = [i + 1 for i in range(n - (n % 2))]
y = [[x[i], x[len(x) - i - 1]] for i in range(len(x) // 2)]
ans = []
for i in range(len(y) - 1):
    for j in range(2):
        for k in range(2):
            ans.append([y[i][j], y[i + 1][k]])
if n == 3:
    ans = [[1, 3], [2, 3]]
elif n == 4:
    ans = [[1, 2], [1, 3], [2, 4], [3, 4]]
elif n % 2 == 1:
    for i in range(len(x) - 1, len(x) + 1):
        for j in range(2):
            ans.append([y[i % len(y)][j], n])
else:
    for i in range(2):
        for j in range(2):
            ans.append([y[len(y) - 1][i], y[0][j]])
print(len(ans))
for ans0 in ans:
    print(" ".join(map(str, ans0)))