import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    INF = 10**18
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())
    SI = lambda : sys.stdin.readline().rstrip()

    N = NI()
    dq = [LI() for _ in range(N)]
    p = [0] * N
    cnt = 0
    c = [0] * N
    while cnt < N*(N-1)//2:
        ud = False
        for i in range(N):

            while p[i] < N-1:
                j = dq[i][p[i]]-1
                if dq[j][p[j]]-1 == i:
                    c[i] = c[j] = max(c[i],c[j]) + 1
                    p[i] += 1; p[j] += 1
                    cnt += 1
                    ud = True
                else:
                    break
        if ud:
            continue
        else:
            print(-1)
            return
    print(max(c))

if __name__ == '__main__':
    main()