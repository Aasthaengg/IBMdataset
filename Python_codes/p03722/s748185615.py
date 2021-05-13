inf=1e13

def bellmanford(E,N):
    score=[inf for i in range(N)]
    score[0]=0
    for i in range(N-1):
        for edge in E:
            u=edge[0]
            v=edge[1]
            if u!=inf:
                score[v]=min(score[v],score[u]+edge[2])
    temp=score[N-1]
    score = [inf for i in range(N)]
    score[0] = 0
    for i in range(N):
        for edge in E:
            u=edge[0]
            v=edge[1]
            if u!=inf:
                score[v]=min(score[v],score[u]+edge[2])
    loop=(temp!=score[N-1])

    return temp,loop


if __name__ == '__main__':
    N,M=list(map(int, input().split()))
    E=[list(map(int, input().split())) for _ in range(M)]
    negative_E=[]
    for a,b,c in E:
        negative_E.append((a-1,b-1,-c))

    score,loop=bellmanford(negative_E,N)
    if loop:
        print("inf")
    else:
        print(-score)