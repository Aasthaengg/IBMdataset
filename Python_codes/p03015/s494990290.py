import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    INF = 10**18
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())
    SI = lambda : sys.stdin.readline().rstrip()

    L = SI()
    n = len(L)
    b = 1
    ans = 1
    for i in range(len(L)):
        if L[n-i-1] == '1':
            ans = (ans*2 + b) % MOD
        b = (b * 3) % MOD
    print((ans)%MOD)

if __name__ == '__main__':
    main()