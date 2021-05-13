MOD = 10**9 + 7
def main():
    n = int(input())
    c = [int(input()) for _ in range(n)]
    d = []
    d.append(c[0])
    for i in range(1, n):
        if c[i] != d[len(d)-1]:
            d.append(c[i])
    lst = [-1]*(2*10**5+1)
    dp = [0]*len(d)
    dp[0] = 1
    lst[d[0]] = 0
    for i in range(1, len(d)):
        if lst[d[i]] == -1:
            lst[d[i]] = i
            dp[i] += dp[i-1]
        else:
            dp[i] += dp[i-1] + dp[lst[d[i]]]
            lst[d[i]] = i
        dp[i] %= MOD
    print(dp[len(d)-1])

if __name__ == "__main__":
    main()