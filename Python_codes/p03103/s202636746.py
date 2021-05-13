n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

ans, buy = 0, 0
for i, j in sorted(a, key=lambda x:x[0]):
    tmp = min(m-buy, j)
    ans += tmp*i
    buy += tmp
    if buy == m: break

print(ans)