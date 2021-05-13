import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    INF = 10**18
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())
    SI = lambda : sys.stdin.readline().rstrip()

    N = NI()
    CMAX = 2*10**5
    A = [0 for _ in range(CMAX+1)]
    S = [1 for _ in range(CMAX+1)]
    C = [NI() for _ in range(N)]
    P = 1
    A[C[0]] = 1
    for i in range(1,N):
        if C[i] != C[i-1] and A[C[i]] > 0:
            S[C[i]] = S[C[i]] + P
        else:
            S[C[i]] = P
        A[C[i]] = 1
        P = S[C[i]] % MOD
    print(P)


if __name__ == '__main__':
    main()