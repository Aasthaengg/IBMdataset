#coding:utf-8

import sys
sys.setrecursionlimit(10**6)
write = sys.stdout.write
dbg = lambda *something : print(*something) if DEBUG else 0
DEBUG = False
def main(given = sys.stdin.readline):
    from collections import defaultdict
    input = lambda : given().rstrip()
    LMIIS = lambda : list(map(int,input().split()))
    II = lambda : int(input())
    XLMIIS = lambda x : [LMIIS() for _ in range(x)]


    P1 = 2**127-1
    P2 = 2**31-1
    P1 = 10**9*7
    P2 = 10**7-9
    base = 26
    N = II()
    S = list(map(ord,list(input())))
    pow1 = [1]*N
    pow2 = [1]*N
    for i in range(N-1):
        pow1[i+1] = pow1[i]*base%P1
        pow2[i+1] = pow2[i]*base%P2
    hash1 = [0]*(N+1)
    hash2 = [0]*(N+1)
    hash1[1] = hash2[1] = S[0]
    for i in range(2,N+1):
        hash1[i] = (hash1[i-1]*base + S[i-1]) % P1
        hash2[i] = (hash2[i-1]*base + S[i-1]) % P2
    
    def f(x):
        hashes = defaultdict(lambda : -1)
        for i in range(N-x+1):
            #S[i:i+x]
            h1 = (hash1[i+x] - hash1[i] * pow1[x]) % P1
            h2 = (hash2[i+x] - hash2[i] * pow2[x]) % P2
            if hashes[(h1,h2)] == -1:
                hashes[(h1,h2)] = i
            elif hashes[(h1,h2)] + x <= i:
                return True
        # print(hashes)
        return False
    
    ok = -1
    ng = N//2+1
    while ng-ok > 1:
        
        m = (ok+ng)//2
        # print(m)
        if f(m):
            ok = m
        else:
            ng = m
    print(ok)

if __name__ == '__main__':
    main()