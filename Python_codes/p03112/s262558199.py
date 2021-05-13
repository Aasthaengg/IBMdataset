import sys,queue,math,copy,itertools,bisect,collections,heapq
sys.setrecursionlimit(10**7)
INF = 10**18
MOD = 10**9 + 7
LI = lambda : [int(x) for x in sys.stdin.readline().split()]
_LI = lambda : [int(x)-1 for x in sys.stdin.readline().split()]
NI = lambda : int(sys.stdin.readline())

A,B,Q = LI()
s = [NI() for _ in range(A)]
t = [NI() for _ in range(B)]
x = [NI() for _ in range(Q)]

s.sort()
t.sort()
s = [-2*INF,-INF] + s + [INF,2*INF]
t = [-2*INF,-INF] + t + [INF,2*INF]

for p in x:
    ans = INF

    si = bisect.bisect_left(s,p)
    s1 = s[si-1]
    s2 = s[si]

    ti1 = bisect.bisect_left(t,s1)
    t11 = t[ti1-1]
    ans = min(ans,p - t11)
    t12 = t[ti1]
    ans = min(ans,(p - s1) + (t12 - s1)  * (t12 > p))

    ti2 = bisect.bisect_left(t,s2)
    t21 = t[ti2-1]
    ans = min(ans,(s2 - p) + (s2 - t21) * (t21 < p))
    t22 = t[ti2]
    ans = min(ans, t22 - p)

    ti = bisect.bisect_left(t, p)
    t1 = t[ti - 1]
    t2 = t[ti]

    si1 = bisect.bisect_left(s, t1)
    s11 = s[si1 - 1]
    ans = min(ans, p - s11)
    s12 = s[si1]
    ans = min(ans, (p - t1) + (s12 - t1) * (s12 > p))

    si2 = bisect.bisect_left(s, t2)
    s21 = s[si2 - 1]
    ans = min(ans, (t2 - p) + (t2 - s21) * (s21 < p))
    s22 = s[si2]
    ans = min(ans, s22 - p)

    print (ans)

