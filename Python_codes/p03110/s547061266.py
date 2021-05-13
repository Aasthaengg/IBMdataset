N = int(input())

ans = 0
for i in range(N):
    X, U = map(str, input().split())
    if U == 'BTC':
        X = float(X)*380000
    ans += float(X)

print(ans)