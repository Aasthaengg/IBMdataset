
N, M = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

X.sort()
res = M
ans = 0
for a, b in X:
    if res <= 0:
        break

    tmp = min(b, res)
    res -= tmp
    ans += tmp * a

print(ans)
