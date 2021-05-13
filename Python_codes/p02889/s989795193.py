import sys
def main():
    input=sys.stdin.readline
    n,m,l=map(int,input().split())
    edge=[[] for i in range(n)]
    for _ in range(m):
        a,b,c=map(int,input().split())
        if c>l:
            continue
        a-=1
        b-=1
        edge[a].append((c,b))
        edge[b].append((c,a))
    def dijkstra(s):
        used=[False for _ in range(n)]
        dist=[(10**18,10**18) for _ in range(n)]
        dist[s]=(0,0)
        for _ in range(n):
            (time,cons),x=min([(dist[i],i) for i in range(n) if not used[i]])
            used[x]=True
            for cost,nx in edge[x]:
                ntime,ncons=dist[nx]
                if l-cons>=cost:
                    if ntime>time:
                        dist[nx]=(time,cons+cost)
                    elif ntime==time:
                        if ncons>cons+cost:
                            dist[nx]=(time,cons+cost)
                else:
                    if ntime>time+1:
                        dist[nx]=(time+1,cost)
                    elif ntime==time+1:
                        if ncons>cost:
                            dist[nx]=(ntime,cost)
        return dist
    ans=[]
    #print(edge)
    for s in range(n):
        ans.append(dijkstra(s))
    q=int(input())
    for _ in range(q):
        s,t=map(int,input().split())
        s-=1
        t-=1
        if ans[s][t][0]==10**18:
            print(-1)
        else:
            print(ans[s][t][0])
if __name__=="__main__":
  main()