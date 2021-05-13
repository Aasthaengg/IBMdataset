import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    INF = 10**18
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())
    SI = lambda : sys.stdin.readline().rstrip()

    n,m = LI()
    a = LI()
    match = [0,2,5,5,4,5,6,3,7,6]
    dp = [-1] * (n+1)
    dp[0] = 0
    for i in range(1,n+1):
        for x in a:
            if i < match[x]: continue
            if dp[i-match[x]] < 0: continue
            dp[i] = max(dp[i],dp[i-match[x]]*10+x)
    print(dp[-1])

if __name__ == '__main__':
    main()