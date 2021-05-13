n, k = map(int,input().split())

if (n - 2) * (n - 1) // 2 < k:
    print(-1)
    exit()

ans = []
for i in range(n - 1):
    ans.append((1, i + 2))

cnt = (n - 1) * (n - 2) // 2 - k
for i in range(2, n):
    for j in range(i + 1, n + 1):
        if cnt == 0:break
        ans.append((i, j))
        cnt -= 1
    if cnt == 0:break

print(len(ans))
for i in ans:
    print(*i)