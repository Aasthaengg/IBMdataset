import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def toId(i, j):
    pair = A[i][j]
    if i > pair:
        i, pair = pair, i
    return ids[i][pair]

def dfs(x):
    if dp[x] != -1:
        if done[x]:
            return dp[x]
        else:
            return -1
    dp[x] = 1
    for y in G[x]:
        res = dfs(y)
        if res == -1:
            return -1
        dp[x] = max(dp[x], dfs(y)+1)
    done[x] = True
    return dp[x]

N = int(input())
A = [list(map(lambda x: int(x)-1, input().split())) for i in range(N)]
ids = [[0]*N for i in range(N)]
num = 0
for i in range(N):
    for j in range(N):
        if i < j:
            ids[i][j] = num
            num += 1
allv = N*N
G = [[] for i in range(allv)]
for i in range(N):
    for j in range(N-2):
        G[toId(i,j+1)].append(toId(i,j))
dp = [-1 for i in range(allv)]
done = [False for i in range(allv)]
ans = 0
for i in range(allv):
    res = dfs(i)
    if res == -1:
        print(-1)
        exit()
    ans = max(ans, dfs(i))
print(ans)