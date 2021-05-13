N = int(input())
ans = []
if N % 2 == 0:
    for i in range(1, N):
        for j in range(i+1, N+1):
            if j == (N + 1 - i):
                continue
            ans.append((i, j))
else:
    for i in range(1, N):
        for j in range(i+1, N+1):
            if j == (N - i):
                continue
            ans.append((i, j))
print(len(ans))
for x in ans:
    print(*x)
