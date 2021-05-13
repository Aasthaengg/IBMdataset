am,k= list(map(int,input().split()))
arr = list(map(int,input().split()))
if am == 1:
    print(0)
else:
    dp = [0]
    for i in range(1,am):
        m = 9999999999999
        for g in range(max(i-k,0),i):
            m = min(dp[g] + abs(arr[g]-arr[i]),m)
        dp.append(m)
    print(dp[-1])