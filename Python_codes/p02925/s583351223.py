import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def main():
    n = int(input())

    A = [0]*n
    for i in range(n):
        a = list(map(int, input().split()))
        a = [a_-1 for a_ in a]
        A[i] = a

    g = [[] for i in range(n*(n-1)//2)]
    id = [[[-1] for i in range(n)] for j in range(n)]

    temp = 0
    for i in range(n-1):
        for j in range(i+1, n):
            id[i][j] = temp
            id[j][i] = temp
            temp += 1

    for i in range(n):
        for j in range(n-2):
            g[id[i][A[i][j]]].append(id[i][A[i][j+1]])

    visit = [-1]*(n*(n-1)*2)
    clc = [-1]*(n*(n-1)*2)
    dp = [1]*(n*(n-1)*2)
    def dfs(v):
        if visit[v] != -1:
            if clc[v] == -1:
                return -1
            return dp[v]
        visit[v] = 0
        for u in g[v]:
            res = dfs(u)
            if res == -1:
                return -1
            dp[v] = max(dp[v], res+1)
        clc[v] = 0
        return dp[v]

    ans = 0
    for i in range(n*(n-1)//2):
        res = dfs(i)
        if res == -1:
            print(-1)
            exit()
        ans = max(ans, res)
    print(ans)

if __name__ == '__main__':
    main()