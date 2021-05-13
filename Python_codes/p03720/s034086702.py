n, m = [int(x) for x in input().split()]
ans = [0] * n
for _ in range(m):
    a, b = [int(x) - 1 for x in input().split()]
    ans[a] += 1
    ans[b] += 1
print(*ans)