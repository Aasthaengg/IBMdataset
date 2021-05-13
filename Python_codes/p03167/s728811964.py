import sys
input = sys.stdin.readline
sys.setrecursionlimit(100007)

def main():
    h, w = map(int, input().split())
    grid = [None]*h
    for i in range(h):
        grid[i] = input()
    
    mod = pow(10, 9)+7
    dp = [[0]*w for _ in range(h)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            dp[i][j] %= mod
            if i != h-1 and grid[i+1][j] == ".":
                dp[i+1][j] += dp[i][j]
            if j != w-1 and grid[i][j+1] == ".":
                dp[i][j+1] += dp[i][j]
    
    print(dp[h-1][w-1])
    
if __name__ == "__main__":
    main()
