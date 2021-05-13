import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    INF = 10**18
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())
    SI = lambda : sys.stdin.readline().rstrip()

    L = SI()
    b = 1
    ans = 1
    for s in L[-1::-1]:
        if s == '1':
            ans = (ans*2 + b) % MOD
        b = (b * 3) % MOD
    print(ans)

if __name__ == '__main__':
    main()