def main():
    n, m = map(int, input().split())
    keys = [[None for j in range(2)] for i in range(m)]
    for i in range(m):
        a, b = map(int, input().split())
        keys[i][0] = a
        keys[i][1] = 0
        c = list(map(int, input().split()))
        for j in c:
            keys[i][1] += int(pow(2, j-1))
    dp = [10**9 for i in range(int(pow(2, n)))]
    dp[0] = 0
    for i in range(int(pow(2, n))):
        for j in range(m):
            if dp[i | keys[j][1]] > dp[i] + keys[j][0]:
                dp[i | keys[j][1]] = dp[i] + keys[j][0]
    if dp[int(pow(2, n)) - 1] == 10**9:
        print("-1")
    else:
        print(dp[int(pow(2, n)) - 1])

if __name__ == "__main__":
    main()