n, k = map(int, input().split())
total = n * (n - 1) // 2
ans = total - k
if ans < n - 1: print(-1)
else:
    print(ans)
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if ans == 0: exit()
            ans += -1
            print(i, j)