
def solve():
    dp = [0] * (N+1)
    dp[0] = 1
    for i in range(N):
        for j in range(i+1, min(N,i+2)+1):
            if broken[j]:
                dp[j] += dp[i]
                dp[j] %=  1000000007
    print(dp[-1])

if __name__ == "__main__":
    N,M = list(map(int, input().split()))
    broken = [True] * (N+1)
    for i in range(M):
        a = int(input())
        broken[a] = False
    solve()  
