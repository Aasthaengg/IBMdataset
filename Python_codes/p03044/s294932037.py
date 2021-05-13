from sys import stdin
from collections import deque
def main():
    #入力
    readline=stdin.readline
    n=int(readline())
    G=[[] for _ in range(n+1)]
    for _ in range(n-1):
        u,v,w=map(int,readline().split())
        G[u].append((v,w))
        G[v].append((u,w))

    d=[0]*(n+1)
    flags=[False]*(n+1)
    flags[1]=True
    q=deque([1])
    while len(q)>0:
        now=q.popleft()
        for nex in G[now]:
            if flags[nex[0]]==False:
                flags[nex[0]]=True
                q.append(nex[0])
                d[nex[0]]=d[now]+nex[1]

    for i in range(1,n+1):
        if d[i]%2==0:
            print(0)
        else:
            print(1)

if __name__=="__main__":
    main()