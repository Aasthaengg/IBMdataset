def main():
    N, T = (int(i) for i in input().split())
    AB = [[int(i) for i in input().split()] for j in range(N)]
    AB.sort()

    ans = 0
    dp1 = [[0]*(T+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(T):
            t = j - AB[i][0]
            if 0 <= t:
                dp1[i+1][j] = max(dp1[i][j], dp1[i][t] + AB[i][1])
            else:
                dp1[i+1][j] = dp1[i][j]
        ans = max(ans, dp1[i][T-1] + AB[i][1])
    print(ans)


if __name__ == '__main__':
    main()
