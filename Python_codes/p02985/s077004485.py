import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    INF = 10**18
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())
    SI = lambda : sys.stdin.readline().rstrip()

    N,K = LI()
    root = [[] for _ in range(N)]
    for _ in range(N-1):
        a,b = LI()
        root[a-1].append(b-1)
        root[b-1].append(a-1)

    q = collections.deque()
    q.append((0,K))
    node = [0] * N
    node[0] = 1
    ans = 1
    while q:
        v,c = q.popleft()
        ans = (ans * c) % MOD
        if c < K: c = K-1
        for u in root[v]:
            if node[u] > 0: continue
            c -= 1
            q.append((u,c))
            node[u] = 1
    print(ans)

if __name__ == '__main__':
    main()