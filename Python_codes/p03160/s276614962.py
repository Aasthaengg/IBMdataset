
def main():
    n = int(input())
    h = list(map(int,input().split()))
    dp = [0] * n
    dp[1] = abs(h[1]-h[0])
    for i in range(2,n):
        one_behind = dp[i-1] + abs(h[i-1] - h[i])
        two_behind = dp[i-2] + abs(h[i-2] - h[i])
        dp[i] = min(one_behind,two_behind)
    print(dp[n-1])



if __name__ == '__main__':
    main()
