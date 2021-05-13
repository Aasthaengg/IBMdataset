import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    INF = 10**18
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())

    n = NI()
    a = LI()
    ans = INF
    for s in (1,-1):
        acc = 0
        cnt = 0
        x = s
        for i in range(n):
            acc += a[i]
            if acc * x <= 0:
                cnt += abs(x-acc)
                acc = x
            x = -x
        ans = min(ans,cnt)
    print(ans)


if __name__ == '__main__':
    main()