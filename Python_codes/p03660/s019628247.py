import sys
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10**6)
def even(n): return 1 if n%2==0 else 0

n = int(readline())
g = [[] for i in range(n)] #g[i]:点iに隣接している点のリスト
for i in range(n-1):
    x,y = map(int,readline().split())
    x,y = x-1,y-1
    g[x].append(y)
    g[y].append(x)

dist_fe = [10**10]*n
dist_su = [10**10]*n

dist_fe[0] = 0
dist_su[n-1] = 0

def bfs(d,v,dist):
    for i in g[v]:
        if d[i] == 10**10:
            d[i] = dist+1
            bfs(d,i,dist+1)

bfs(dist_fe,0,0)
bfs(dist_su,n-1,0)

b = 0
w = 0

for i in range(n):
    if dist_fe[i] <= dist_su[i]: #先手優先
        b += 1
    else:
        w += 1

ans = "Fennec" if b > w else "Snuke"
print(ans)