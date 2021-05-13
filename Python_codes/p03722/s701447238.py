n,m=map(int,input().split())
g=[[] for _ in range(n)]
for _ in range(m):
    a,b,c=map(int,input().split())
    g[a-1].append([b-1,-c])

def bellman_ford(g,n):
    INF = 10**15
    res = [INF for _ in range(n)]
    res[0] = 0
    for _ in range(n-1):
        for i in range(n):
            for sa,sb in g[i]:
                res[sa] = min(res[sa],res[i]+sb)
    f = [False for _ in range(n)]
    for _ in range(n+1):
        for i in range(n):
            for sa,sb in g[i]:
                if res[sa] > res[i]+sb:
                    res[sa] = res[i]+sb
                    f[sa] = True
    if f[-1]: return "inf"
    else:return res[-1]*-1

print(bellman_ford(g,n))