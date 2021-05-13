import sys
input = sys.stdin.buffer.readline

def main():
    N,M = map(int,input().split())
    p = {1:2,7:3,4:4,5:5,3:5,2:5,9:6,6:6,8:7}
    a = list(map(int,input().split()))
    INF = float("inf")
    dp = [-INF for _ in range(N+1)]
    dp[0] = 0
    for i in range(N):
        for j in a:
            if i+p[j] <= N:
                dp[i+p[j]] = max(dp[i+p[j]],dp[i]+1)
    
    dp.reverse()
    use = []
    for i in a:
        use.append((i,p[i]))
        
    use.sort(key=lambda x:(-x[0],-x[1]))
    ans = []
    now = 0
    while now < N:
        for num,i in use:
            if (now+i <= N and dp[now+i] == dp[now]-1):
                ans.append(str(num))
                now += i
                break
    print("".join(ans))
    
if __name__ == "__main__":
    main()
