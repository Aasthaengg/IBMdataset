import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    INF = 10**18
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    _LI = lambda : [int(x)-1 for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())
    SI = lambda : sys.stdin.readline().rstrip()
    DD = ((1,0),(0,1),(-1,0),(0,-1))

    n,m = LI()
    x = LI()
    y = LI()

    x.sort()
    y.sort()

    ysum = 0
    for j in range(1,m):
        ysum += j * (m-j) * (y[j]-y[j-1])

    ans = 0
    for i in range(1,n):
        ans = (ans + i * (n-i) * (x[i]-x[i-1]) * ysum) % MOD

    print(ans)
if __name__ == '__main__':
    main()