import sys
input = sys.stdin.readline

def main():
    N = int(input())
    c = [-1]
    INF = 10**9+7
    for _ in range(N):
        a = int(input())
        if c[-1] == a-1:
            continue
        c.append(a-1)
    
    c.pop(0)
    d,M = len(c),max(c)
    dp = [1 for _ in range(d+1)]
    c_dp = [0 for _ in range(M+1)]
    for i in range(d):
        now = c[i]
        dp[i+1] = (dp[i] + c_dp[now])%INF
        c_dp[now] = dp[i+1]
                
    print(dp[-1])
    
if __name__ == "__main__":
    main()
