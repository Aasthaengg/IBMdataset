n, m = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(n)]
AB.sort()

ans = 0
for ab in AB:
    t = min(m, ab[1])
    ans += ab[0]*t
    m -= t

print(ans)