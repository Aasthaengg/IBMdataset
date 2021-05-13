def main():
    n, k = map(int, input().split())
    stones = tuple(map(int, input().split()))
    inf = 10**9
    dp = [inf]*n
    dp[0] = 0
    for i in range(n):
        for t in range(1, k+1):
            step = i+t
            if step < n:
                v = dp[i]+abs(stones[i]-stones[step])
                if v < dp[step]:
                    dp[step] = v
    print(dp[-1])


if __name__ == '__main__':    
    main()
