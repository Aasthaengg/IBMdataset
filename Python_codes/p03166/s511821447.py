import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.buffer.readline

def main():
    n, m = map(int, input().split())
    edges = [[] for _ in range(n)]
    for _ in range(m):
        x, y = map(int, input().split())
        edges[y - 1].append(x - 1)
    used = [False for _ in range(n)]
    dp = [0 for _ in range(n)]
    
    def dfs(pos):
        if not edges[pos]:
            dp[pos] = 0
            return
        for n_pos in edges[pos]:
            if not used[n_pos]:
                dfs(n_pos)
            used[n_pos] = True
            dp[pos] = max(dp[pos], dp[n_pos] + 1)
            
    
    for i in range(n):
        if used[i]:
            continue
        used[i] = True
        dfs(i)
        
    print(max(dp))

main()