import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**7)

def main():
    N = int(input())
    memo = []
    base = 0
    for i in range(N-1):
        memo.append(base)
        base += N-i-1
    edge = [[] for _ in range((N*(N-1))//2)]
    
    for i in range(N):
        a = list(map(int,input().split()))
        b = []
        for j in a:
            j -= 1
            if i < j:
                b.append(memo[i]+j-i-1)
            else:
                b.append(memo[j]+i-j-1)
        for i in range(N-2):
            edge[b[i+1]].append(b[i])

    go = [False]*((N*(N-1))//2)
    cul = [False]*((N*(N-1))//2)
    dp = [0]*((N*(N-1))//2)
    
    def dfs(v):
        if go[v]:
            if not cul[v]:
                return -1
            return dp[v]
        go[v] = True
        dp[v] = 1
        for u in edge[v]:
            ret = dfs(u)
            if ret == -1:
                return -1
            dp[v] = max(dp[v],ret+1)
        cul[v] = True
        return dp[v]
    
    ans = 0
    for i in range((N*(N-1))//2):
        ret = dfs(i)
        if ret == -1:
            print(-1)
            exit()
        ans = max(ans,ret)
        
    print(ans)

if __name__ == "__main__":
    main()