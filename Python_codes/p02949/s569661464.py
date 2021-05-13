import sys
sys.setrecursionlimit(10**5)


def dfs(s):
    for i in to[s]:
        if not toflag[i]:
            toflag[i]=True
            dfs(i)


def rdfs(s):
    for i in ot[s]:
        if not otflag[i]:
            otflag[i]=True
            rdfs(i)


def bellman_ford():
    for i in range(n):
        upd=False
        for a,b,c in edges:
            if d[b]>d[a]+c:
                upd=True
                d[b]=d[a]+c     
        if not upd:
            break
        if i == n-1:
            print(-1)
            exit()


def main():

    for i in range(m):
        a,b,c=map(lambda x:int(x)-1,input().split())
        edges.append([a,b,-(c+1-p)])
        to[a].append(b)
        ot[b].append(a)

    toflag[0]=True
    otflag[n-1]=True
    dfs(0) # check for 0 to i path
    rdfs(n-1) # check for n-1 to i path
 
    for i in range(m):
        a,b,c=edges[i]
        if toflag[a] and otflag[a] and toflag[b] and otflag[b]: continue;
        edges[i]=[0,0,0]

    d[0]=0
    bellman_ford()
    print(max(0,-d[-1]))



if __name__=='__main__':
    n,m,p=map(int,input().split())
    edges=[]
    to=[[] for i in range(n)]
    ot=[[] for i in range(n)]
    toflag=[False]*n
    otflag=[False]*n
    d=[10**9]*n
    main()