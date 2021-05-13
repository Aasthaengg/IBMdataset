def main():
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    mapk = {1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}
    
    dp = [0 for _ in range(N+1)] # ちょうどi本使ったときの最大桁数
    for i in range(1, N+1):
        tmp = []
        for k in lst:
            if (i-mapk[k])>=0:
                tmp.append(dp[i-mapk[k]] + 1)
            else:
                tmp.append(-float('inf'))
        dp[i] = max(tmp)
    #print(dp)
    
    ans = ''
    X = N
    lst = sorted(lst, reverse=True)
    for _ in range(dp[N]):
        for k in lst:
            if (X-mapk[k]>=0) and (dp[X - mapk[k]] == dp[X] - 1):
                ans += str(k)
                X -= mapk[k]
                break
    print(ans)
main()
