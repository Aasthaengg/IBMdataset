import sys
input = sys.stdin.readline
def main():
    n,m = map(int,input().split())
    dp = [[10**10 for _ in range(2**n)] for _ in range(m+1)]
    dp[0][0] = 0
    for i in range(m):
        a,b = map(int,input().split())
        c = list(map(int,input().split()))
        S = 0
        for j in range(b):
            x = pow(2,c[j]-1)
            S |= x
        for j in range(2**n):
            dp[i+1][j] = min(dp[i+1][j],dp[i][j])
        for j in range(2**n):
            dp[i+1][j|S] = min(dp[i+1][j|S],dp[i][j]+a)
    if dp[m][2**n-1] == 10**10:
        print(-1)
    else:
        print(dp[m][2**n-1])

if __name__ == "__main__":
    main()