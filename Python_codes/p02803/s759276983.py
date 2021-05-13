# floyd_warshall
h,w = map(int,input().split())
l = [['#']*(w+2)]
for i in range(h):
    l.append(['#']+list(input())+['#'])
l.append(['#']*(w+2))

def id(x,y):
    return x*w+y

INF = 1<<29
dp = [[INF]*500 for _ in range(500)]
for i in range(500):
    dp[i][i] = 0


ans = 0
directions = [(1,0),(0,1),(-1,0),(0,-1)]

for i in range(1,h+1):
    for j in range(1,w+1):
        if l[i][j]=='#':
            continue
        for dir in directions:
            ni = i+dir[0]
            nj = j+dir[1]
            if l[ni][nj] == '#':
                continue
            dp[id(i-1,j-1)][id(ni-1,nj-1)] = 1
            dp[id(ni-1,nj-1)][id(i-1,j-1)] = 1

for k in range(h*w):
    for i in range(h*w):
        for j in range(h*w):
            dp[i][j] = min(dp[i][j],dp[i][k]+dp[k][j])

ans = 0
for si in range(h):
    for sj in range(w):
        if l[si+1][sj+1] == '#':
            continue
        for gi in range(h):
            for gj in range(w):
                if l[gi+1][gj+1] == '#':
                    continue
                ans = max(ans,dp[id(si,sj)][id(gi,gj)])
print(ans)