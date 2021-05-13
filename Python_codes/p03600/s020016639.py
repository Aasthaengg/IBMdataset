from heapq import heappush, heappop
def main():
    N=int(input())
    road=[[float("inf") for _ in range(N)]for _ in range(N)]
    pq=[]
    ans=0
    for i in range(N):
        road[i][i]=0
        tmp=list(map(int,input().split()))
        for j in range(i+1,N):
            heappush(pq,(tmp[j],i,j))

    while pq:
        v=heappop(pq)
        d,i,j=v[0],v[1],v[2]
        tmp=road[i][j]
        for k in range(N):
            tmp=min(tmp,road[i][k]+road[k][j])
            if tmp==d:
                break
        if tmp>d:
            road[i][j]=d
            road[j][i]=d
            ans+=d
        elif tmp==d:
            road[i][j]=d
            road[j][i]=d
        else:
            print(-1)
            exit()
    print(ans)
main()