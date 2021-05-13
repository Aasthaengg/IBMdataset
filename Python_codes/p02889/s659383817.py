import sys

sys.setrecursionlimit(500000)
def input():
    return sys.stdin.readline()[:-1]

def main():
    N,M,L = list(map(int,input().split()))
    e_list = [[] for i in range(N)]
    for i in range(M):
        A,B,C = list(map(int,input().split()))
        A,B = A-1,B-1
        e_list[A].append((B,C))
        e_list[B].append((A,C))

    INF = float('inf')
    D = [[INF]*N for i in range(N)]
    for i in range(N):
        for j,d in e_list[i]:
            D[i][j]=d

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if D[i][j]>D[i][k]+D[k][j]:
                    D[i][j] = D[i][k]+D[k][j]

    E = [[INF]*N for i in range(N)]

    for i in range(N):
        for j in range(N):
            if D[i][j]<=L:
                E[i][j]=1

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if E[i][j]>E[i][k]+E[k][j]:
                    E[i][j] = E[i][k]+E[k][j]

    Q = int(input())
    for i in range(Q):
        s,t = list(map(int,input().split()))
        s,t = s-1,t-1
        if E[s][t]>10**28:
            print(-1)
        else:
            print(E[s][t]-1)
            
if __name__ == '__main__':
    main()

