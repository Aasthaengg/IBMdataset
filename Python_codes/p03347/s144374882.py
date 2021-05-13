import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    INF = 10**18
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())
    SI = lambda : sys.stdin.readline().rstrip()

    N = NI()
    A = [NI() for _ in range(N)]

    ans = 0
    cnt = 0
    for i in range(N-1,-1,-1):
        if cnt == 0:
            ans += A[i]
            cnt = A[i]
        elif A[i] < cnt -1:
            print(-1)
            return
        elif A[i] >= cnt:
            ans += A[i]
            cnt = A[i]
        else:
            cnt -= 1
    if cnt > 0:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()