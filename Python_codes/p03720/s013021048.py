n, m = map(int, input().split())
loads = [list(map(int, input().split())) for _ in range(m)]
ans = [0] * (n + 1)
for i in range(m):
    for j in loads[i]:
        ans[j] += 1
for out in range(1, n + 1):
    print(ans[out])
