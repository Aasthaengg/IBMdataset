def main():
    n = int(input())
    a = sorted(list(map(int,input().split())))
    dp = [0 for i in range(a[-1]+1)]
    lbl = []
    for i in range(n):
        if dp[a[i]]==2:
            lbl.append(a[i])
            continue
        if dp[a[i]]==1:
            continue
        else:
            for j in range(1,a[-1]//a[i]+1):
                dp[a[i]*j] = 1
            dp[a[i]] = 2
    for i in range(len(lbl)):
        dp[lbl[i]] = 0
    ans = 0
    for i in range(len(dp)):
        if dp[i] == 2:
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()
