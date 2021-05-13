mod = 1e9+7
def add(a, b):
    c = a + b
    if c >= mod:
        c -= mod
    return c
"""
Given H and N pairs, pairs[0] is attack while pairs[1] is cost. H is the monster health. Find the
minimum cost to get to H

knapsack

dp[i][j] - Minimum cost to reach up to j, such that only first i-th elements are considered

For each new element, its optimal is
dp[i][j] = max(dp[i-1][j-cost[i]], dp[i-1][j])
"""
def main():
    INF = 1e9 + 7
    H, N = [int(x) for x in raw_input().split()]
    value = [0 for _ in range(N)]
    cost = [0 for _ in range(N)]
    
    for i in range(N):
        A, B = [int(x) for x in raw_input().split()]
        value[i] = A
        cost[i] = B
    
    #dp = [[0 for _ in range(H+1)] for _ in range(N)]
    dp = [INF for _ in range(H+1)]
    
    dp[0] = 0
    
    for i in range(N):
        #new_dp = [INF for j in range(H+1)]
        for j in range(H+1):
            after_health = max(0, j - value[i])
            dp[j] = min(dp[after_health] + cost[i], dp[j])
        #dp = new_dp
            
            
    print(dp[H])
    

main()