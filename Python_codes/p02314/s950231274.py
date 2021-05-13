n, m = map(int, input().split())
c = list(map(int, input().split()))
dp = [[0],[i for i in range(n+1)]]
for mi in range(1, m):
    dp.append([0])
    coin = c[mi]
    for ni in range(1, n+1):
        if ni>=coin:
            dp[-1].append(min(dp[-1][-c[mi]]+1,dp[-2][ni]))
        else:
            dp[-1].append(dp[-2][ni])
print(dp[-1][n])
