import sys,queue,math,copy,itertools,bisect,collections,heapq


def wf(d,n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

def main():
    INF = 10**18
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())

    N,M,L = LI()
    road = [[INF] * N for _ in range(N)]
    for _ in range(M):
        a,b,c = LI()
        if c <= L:
            road[a-1][b-1] = c
            road[b-1][a-1] = c

    road = wf(road,N)


    gas = [[INF] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if road[i][j] <= L:
                gas[i][j] = 1

    gas = wf(gas,N)

    Q = NI()
    for _ in range(Q):
        s,t = LI()
        if gas[s-1][t-1] == INF:
            print(-1)
        else:
            print(gas[s-1][t-1]-1)


if __name__ == '__main__':
    main()