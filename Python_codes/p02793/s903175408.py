import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    INF = 10**18
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())

    N = NI()
    A = LI()
    d = [0] * (max(A)+1)

    for x in A:
        for i in range(2,int(math.sqrt(x))+1):
            cnt = 0
            while x % i == 0:
                cnt += 1
                x //= i
            d[i] = max(d[i],cnt)
            if x == 1: break
        else:
            d[x] = max(1,d[x])
    m = 1
    for i in range(2,len(d)):
        m = (m * i ** d[i]) % MOD
    ans = 0
    for x in A:
        ans += (m * pow(x,MOD-2,MOD)) % MOD
    print(ans % MOD)


if __name__ == '__main__':
    main()