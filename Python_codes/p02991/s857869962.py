import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    INF = 10**6
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())
    SI = lambda : sys.stdin.readline().rstrip()

    N,M = LI()
    root = [[] for _ in range(N)]
    node = [[INF,INF,INF] for _ in range(N)]
    for _ in range(M):
        a,b = LI()
        root[a-1].append(b-1)
    S,T = LI()
    S -= 1; T -= 1
    q = collections.deque()
    q.append((S,0,0))
    node[S][0] = 0
    while q:
        v,n,d = q.popleft()
        t = (n+1) % 3
        for u in root[v]:
            if node[u][t] > d+1:
                node[u][t] = d+1
                q.append((u,t,d+1))
    if node[T][0] < INF:
        print(node[T][0]//3)
    else:
        print(-1)


if __name__ == '__main__':
    main()