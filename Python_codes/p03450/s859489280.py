def solve():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    INF=float('inf')
    n,m=map(int,input().split())
    l=[list(map(int,input().split())) for _ in range(m)]
    d=[INF]*n
    nbr=[[] for _ in range(n)]
    used=[False]*m
    for x in l:
        x[0]-=1
        x[1]-=1
    #print(l)
    for i in range(m):
        nbr[l[i][0]].append(i)
        nbr[l[i][1]].append(i)
    #print(nbr)
    def sol(i):
        for x in nbr[i]:
            if used[x]:continue
            used[x]=True
            i1=l[x][0]^l[x][1]^i
            dd=d[i]+l[x][2]*(2*(l[x][0]==i)-1)
            if d[i1]!=dd and d[i1]!=INF:
                print('No')
                exit()
            elif d[i1]==INF:
                d[i1]=dd
                sol(i1)
    for i in range(n):
        if d[i]==INF:
            d[i]=0
            sol(i)
    #print(d)
    print('Yes')
solve()