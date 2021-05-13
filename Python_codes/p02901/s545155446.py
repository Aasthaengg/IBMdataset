#142_E
n, m = map(int, input().split())
inf = 10 ** 10
keys = [0 for _ in range(m)]
A = [] 

for i in range(m):
    a, _ = map(int, input().split())
    keys[i] = sum([2 ** (int(c) - 1) for c in input().split()])
    A.append(a)
    
dp = [[inf for _ in range(2 ** n)] for _ in range(m+1)]
dp[0][0] = 0
for i in range(0, m):
    for key in range(2 ** n):
        dp[i+1][key] = dp[i][key]
        
    for key in range(2 ** n):
        dp[i+1][key | keys[i]] = min(dp[i+1][key | keys[i]],
                                     dp[i][key] + A[i])

if dp[m][2 ** n - 1] == inf:
    print(-1)
else:
    print(dp[m][2 ** n - 1])