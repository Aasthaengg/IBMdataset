def inpl(): return list(map(int, input().split()))
N, M = inpl()
X = sorted([inpl() for _ in range(N)], key=lambda x: -x[0])
ans = 0
while M:
    a, b = X.pop()
    buy = min(M, b)
    ans += a*buy
    M -= buy
print(ans)