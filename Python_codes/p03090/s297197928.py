N = int(input())
ans = []
if N % 2 == 0:
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if j <= i or i + j == N + 1:
                continue
            ans.append((i, j))
else:
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if j <= i or i + j == N:
                continue
            ans.append((i, j))

print(len(ans))
for i, j in ans:
    print(i, j)
