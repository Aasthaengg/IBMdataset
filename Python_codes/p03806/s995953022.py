import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    INF = 10**5
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]

    n,ma,mb = LI()
    med = [LI() for _ in range(n)]
    h1 = [INF] * 10000

    for i in range(1,2 ** (n//2)):
        bit = 1
        ta = 0
        tb = 0
        tc = 0
        for j in range(n//2):
            if i & bit:
                a,b,c = med[j]
                ta += a
                tb += b
                tc += c
            bit <<= 1
        dif = ta * mb - tb * ma
        if h1[dif] > tc: h1[dif] = tc

    ans = h1[0]

    for i in range(1,2 ** (n - n//2)):
        bit = 1
        ta = 0
        tb = 0
        tc = 0
        for j in range(n - n//2):
            if i & bit:
                a,b,c = med[j+n//2]
                ta += a
                tb += b
                tc += c
            bit <<= 1
        dif = tb * ma - ta * mb
        if dif == 0:
            ans = min(ans,tc)
        else:
            ans = min(ans,h1[dif]+tc)

    if ans < INF:
        print(ans)
    else:
        print(-1)

if __name__ == '__main__':
    main()