import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    INF = 10**19
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())
    SI = lambda : sys.stdin.readline().rstrip()

    N = NI()
    AB = [LI() for _ in range(N)]
    d = {}

    ans = 0
    zero = 0
    for i in range(N):
        a,b = AB[i]
        if a == 0:
            if b == 0:
                zero += 1
                continue
            b = 1
            s = 1
        elif b == 0:
            a = 1
            s = -1
        else:
            s = (a*b>0) - (a*b<0)
            a = abs(a); b = abs(b)
            x = math.gcd(a,b)
            a = a // x; b = b // x
        if (a,b,s) in d:
            d[(a,b,s)] += 1
        else:
            d[(a,b,s)] = 1

    ans = 1
    for (a,b,s),data in d.items():
        if data == 0: continue
        if (b, a, -s) in d:
            m = d[(b,a,-s)]
            d[(b, a, -s)] = 0
        else:
            m = 0
        x = pow(2,data,MOD) + pow(2,m,MOD) - 1
        ans = (ans * x) % MOD

    print((ans-1+zero)%MOD)

if __name__ == '__main__':
    main()