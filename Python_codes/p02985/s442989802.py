import sys
input = sys.stdin.readline

def main():
    n,k = map(int,input().split())
    mod = 10**9+7
    edge = [[] for _ in [None]*n]

    for _ in [None]*(n-1):
        a,b = map(int,input().split())
        edge[a-1].append(b-1)
        edge[b-1].append(a-1)
    
    p = -1
    pl = -1
    for i in range(n-1):
        if len(edge[i]) > pl:
            p = i
            pl = len(edge[i])
    
    par = [-2]*n
    par[p] = -1
    tank = []
    new = [p]
    while len(new) > 0:
        tank = []
        for e in new:
            for ko in edge[e]:
                if par[ko] == -2:
                    par[ko] = e
                    tank.append(ko)
        new = tank
    
    d = [-1]*n
    d[p] = k
    tank = []
    new = [p]
    while len(new) > 0:
        tank = []
        for e in new:
            if e == p:
                cnt = 1
            else:
                cnt = 2
            for go in edge[e]:
                if go != par[e]:
                    d[go] = k-cnt
                    cnt += 1
                    tank.append(go)
        new = tank
    
    res = 1
    for e in d:
        res = res*e%mod
    print(res)

if __name__ == '__main__':
    main()