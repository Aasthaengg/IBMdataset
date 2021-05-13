import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    INF = 10**5
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())
    SI = lambda : sys.stdin.readline().rstrip()

    N = NI()
    A = LI()
    A.sort(reverse=True)
    p = []
    for i in range(1,len(A)-1):
        if A[i] < 0: break
        p.append((A[-1],A[i]))
        A[-1] -= A[i]
        A[i] = INF
    for a in A[1:]:
        if a < INF:
            p.append((A[0],a))
            A[0] -= a
    print(A[0])
    for a in p:
        print(a[0],a[1])


if __name__ == '__main__':
    main()