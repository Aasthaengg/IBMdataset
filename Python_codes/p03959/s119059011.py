import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    INF = 10**9
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())

    N = NI()
    T = LI()
    A = LI()
    T = [0] + T + [T[-1]]
    A = [A[0]] + A + [0]

    ans = 1
    for i in range(1,N+1):
        m = 0
        if T[i] > T[i-1]:
            tmp1 = 1
            m1 = T[i]
        else:
            tmp1 = T[i]
            m1 = 1
        if A[i] > A[i+1]:
            tmp2 = 1
            m2 = A[i]
        else:
            tmp2 = A[i]
            m2 = 1

        if m1 <= m2 < m1 + tmp1 or m2 <= m1 < m2 + tmp2:
            tmp = min(tmp1,tmp2)
        else:
            tmp = 0
        ans = (ans * tmp) % MOD
    print(ans)

if __name__ == '__main__':
    main()