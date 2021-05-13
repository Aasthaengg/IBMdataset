
from itertools import permutations


def submit():
    n, m, _ = map(int, input().split())
    rlist = list(map(int, input().split()))
    rlist = [r - 1 for r in rlist]

    # warshall floyd
    dp = [[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0
    for _ in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        dp[a][b] = dp[b][a] = c

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    
    min_cost = float('inf')
    for pt in permutations(rlist):
        cost = 0
        for i in range(len(pt) - 1):
            cost += dp[pt[i]][pt[i + 1]]
        
        if min_cost > cost:
            min_cost = cost

    print(min_cost)


submit()