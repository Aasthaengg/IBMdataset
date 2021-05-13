import sys
input = sys.stdin.readline
sys.setrecursionlimit(100007)

def main():
    n, m = map(int, input().split())
    
    grid = [[] for _ in range(n)]
    
    for _ in range(m):
        x, y = map(int, input().split())
        grid[x-1].append(y-1)
    
    memo = [-1]*n
    
    def dp(n):
        if memo[n] != -1:
            return memo[n]
        res = 0
        for v in grid[n]:
            res = max(res, dp(v)+1)
        memo[n] = res
        return res
    
    ans = 0
    for i in range(n):
        sub = dp(i)
        if ans < sub:
            ans = sub
        
    print(ans)
    
    
    
if __name__ == "__main__":
    main()
