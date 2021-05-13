n, k, s = map(int, input().split())
if k == 0:
    ans = [s + 1 for _ in range(n)] if s != 10**9 else [1 for _ in range(n)]
    print(*ans)
else:
    ans = [s + 1 for _ in range(n)] if s != 10**9 else [1 for _ in range(n)]
    for i in range(k):
        ans[i] = s
    print(*ans)
