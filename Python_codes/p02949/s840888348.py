import sys
def main():
    input = sys.stdin.readline
    N,M,P=map(int, input().split())
    E=[]
    G=[[] for _ in range(N)]
    H=[[] for _ in range(N)]
    for _ in range(M):
        a,b,c=map(int, input().split())
        a,b=a-1,b-1
        E.append((a,b,c-P))
        G[b].append(a)
        H[a].append(b)

    R1=[False]*N
    R1[0]=True
    stk=[0]
    while stk:
        v=stk.pop()
        for to in H[v]:
            if R1[to]: continue
            R1[to]=True
            stk.append(to)

    R2=[False]*N
    R2[N-1]=True
    stk=[N-1]
    while stk:
        v=stk.pop()
        for to in G[v]:
            if R2[to]: continue
            R2[to]=True
            stk.append(to)

    INF=10**10
    d=[-INF]*N
    d[0]=0
    for i in range(N):
        for a,b,c in E:
            if R1[a]==False: continue
            if R2[b]==False: continue
            if d[a]==-INF: continue
            if d[b] < d[a] + c:
                d[b] = d[a] + c
                if i==N-1:
                    print(-1)
                    return
    print(max(0,d[N-1]))

if __name__ == '__main__':
    main()