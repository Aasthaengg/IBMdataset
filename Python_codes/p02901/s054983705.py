def resolve():
    N, M = list(map(int, input().split()))
    costs = []
    openables = []
    for i in range(M):
        a, b = list(map(int, input().split()))
        costs.append(a)
        C = list(map(int, input().split()))
        state = 0
        for c in C:
            state += (1<<(c-1))
        openables.append(state)
    
    dp = [[float("inf") for _ in range(4100)] for __ in range(10**3+100)]
    dp[0][0] = 0
    for i in range(M):
        for j in range(1<<N):
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])
            opened_boxes = openables[i]
            dp[i+1][j|opened_boxes] = min(dp[i+1][j|opened_boxes], dp[i][j]+costs[i])
    print(dp[M][(1<<N)-1] if dp[M][(1<<N)-1] < float("inf") else -1)

if __name__ == "__main__":
    resolve()