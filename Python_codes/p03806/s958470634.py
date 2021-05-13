import sys
input = sys.stdin.readline

n, ma, mb = map(int, input().split())
abc = [list(map(int, input().split())) for _ in range(n)]

dp = [5000 for i in range(170000)]
dp[0] = 0

for a, b, c in abc:
    dpn = dp[:]
    for i in range(170000):
        nex = 401 * b + a + i
        if nex >= 170000:
            break
        dpn[nex] = min(dpn[nex], dp[i] + c)
    dp = dpn

ans = 50000

for i in range(1,170000):
    a = i % 401
    b = i // 401
    if ma * b == mb * a:
        ans = min(ans, dp[i])

if ans == 5000:
    print(-1)
else:
    print(ans)

