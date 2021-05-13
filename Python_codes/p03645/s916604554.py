from sys import stdin
from collections import deque
def main():
    #入力
    readline=stdin.readline
    n,m=map(int,readline().split())
    G=[[] for _ in range(n+1)]
    for _ in range(m):
        a,b=map(int,readline().split())
        G[a].append(b)
        G[b].append(a)

    #bfs
    q=deque([tuple((1,0))])
    flags=[False]*(n+1)
    flags[1]=True
    ans=False
    while len(q)>0:
        now,d=q.popleft()
        if now==n:
            if d==2:
                ans=True
                break
        for nex in G[now]:
            if flags[nex]==False:
                flags[nex]=True
                q.append(tuple((nex,d+1)))

    print("POSSIBLE" if ans else "IMPOSSIBLE")

if __name__=="__main__":
    main()