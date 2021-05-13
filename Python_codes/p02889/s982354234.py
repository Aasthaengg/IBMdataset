import sys
sys.setrecursionlimit(10**9)
INF=10**18
def input():
    return sys.stdin.readline().rstrip()

def main():
    N,M,L=map(int,input().split())
    d=[[INF]*N for _ in range(N)]
    for _ in range(M):
        A,B,C=map(lambda x:int(x)-1,input().split())
        d[A][B]=C+1
        d[B][A]=C+1
    Q=int(input())
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    d2=[[INF]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if d[i][j]<=L:
                d2[i][j]=1
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d2[i][j]=min(d2[i][j],d2[i][k]+d2[k][j])
    for _ in range(Q):
        s,t=map(lambda x:int(x)-1,input().split())
        dist=d2[s][t]
        if dist>=INF:
            print(-1)
        else:
            print(dist-1)
            
if __name__ == '__main__':
    main()
