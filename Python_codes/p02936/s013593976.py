import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n,q = map(int,input().split())
ab = [list(map(int,input().split()))for i in range(n-1)]
px = [list(map(int,input().split()))for i in range(q)]

def dfs(m):
    for i in range(len(adj[m])):
        if depth[adj[m][i]] == float('inf'):
            depth[adj[m][i]] = depth[m] + 1
            point[adj[m][i]] += point[m]
            dfs(adj[m][i])


point = [0]*(n+1)
depth = [float('inf')]*(n+1)
adj = [[]for _ in range(n+1)]

for i in range(n-1):
    adj[ab[i][0]].append(ab[i][1])
    adj[ab[i][1]].append(ab[i][0])

for i in range(q):
    point[px[i][0]] += px[i][1]

depth[1] = 1
dfs(1)

for i in range(1,n+1):
    print(point[i],end = ' ')










'''
n,q = map(int,input().split())
ab = [list(map(int,input().split()))for i in range(n-1)]
px = [list(map(int,input().split()))for i in range(q)]

def dfs(m):
    if m in vdic:
        for i in range(len(vdic[m])):
            point[vdic[m][i]] += point[m]
            dfs(vdic[m][i])

point = [0]*(n+1)

vdic = {}
for i in range(n-1):
    if ab[i][0] not in vdic:
        vdic[ab[i][0]] = []
    vdic[ab[i][0]].append(ab[i][1])

for i in range(q):
    point[px[i][0]] += px[i][1]

dfs(1)

for i in range(1,len(point)):
    print(point[i],end = ' ')

'''