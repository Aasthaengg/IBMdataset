import sys
input = sys.stdin.readline
n,m,q = map(int,input().split())
def func(a):
    return int(a)-1
grid = [[0]*n for i in range(n)]
pq = [0]*q
for i in range(m):
    l,r = map(func,input().split())
    grid[l][r] += 1
for i in range(q):
    pq[i] = list(map(func,input().split()))

s = [[0]*n for i in range(n)]
s[0][0] = grid[0][0]
for i in range(1,n):
    s[i][0] = s[i-1][0] + grid[i][0]
for i in range(1,n):
    s[0][i] = s[0][i-1] + grid[0][i]

for i in range(1,n):
    for j in range(1,n):
        s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + grid[i][j]

anslist = [0]*q
for i in range(q):
    anslist[i] = s[pq[i][1]][pq[i][1]] - s[pq[i][1]][pq[i][0]-1] - s[pq[i][0]-1][pq[i][1]] + s[pq[i][0]-1][pq[i][0]-1] if pq[i][0] > 0 else s[pq[i][1]][pq[i][1]]
#print(grid)
#print(s)
for ans in anslist:
    print(ans)
