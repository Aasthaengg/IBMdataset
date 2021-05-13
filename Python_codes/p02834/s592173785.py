import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    INF = 10**6
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())
    SI = lambda : sys.stdin.readline().rstrip()

    N,u,v = LI()
    root = [[] for _ in range(N)]
    for _ in range(N-1):
        a,b = LI()
        root[a-1].append(b-1)
        root[b-1].append(a-1)
    T = [INF for _ in range(N)]
    A = [INF for _ in range(N)]

    def calc_d(m,x):
        q = collections.deque()
        q.append((x,0))
        while q:
            a,d = q.popleft()
            m[a] = d
            for b in root[a]:
                if m[b] > d+1:
                    q.append((b,d+1))

    calc_d(T,u-1)
    calc_d(A,v-1)
    ans = 0
    for i in range(N):
        if T[i] < A[i]:
            ans = max(ans,A[i] - 1)
    print(ans)

if __name__ == '__main__':
    main()