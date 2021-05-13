N = int(input())
bad = N if N % 2 else N + 1
ans = []
for i in range(1, N):
    for j in range(i + 1, N + 1):
        if i + j == bad:
            continue
        ans.append((i, j))
print(len(ans))

for x, y in ans:
    print(x, y)
