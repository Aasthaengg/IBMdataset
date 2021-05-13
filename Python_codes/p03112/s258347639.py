import bisect
INF = 10**13
A, B, Q = map(int, input().split())
S = [int(input()) for a in range(A)]
T = [int(input()) for b in range(B)]
for q in range(Q):
    x = int(input())
    si = bisect.bisect_left(S, x)
    ti = bisect.bisect_left(T, x)
    Sq = [S[max(si-1, 0)], S[min(si, A-1)]]
    Tq = [T[max(ti-1, 0)], T[min(ti, B-1)]]
    ans = float('inf')
    for i in range(2):
        for j in range(2):
            s = Sq[i]
            t = Tq[j]
            if (s < x and t < x) or (x < s and x < t):
                xs, tx = abs(x-s), abs(x-t)
                ans = min(ans, max(xs, tx))
            else:
                xs, tx = abs(s-x), abs(t-x)
                ans = min(ans, min(xs, tx)*2 + max(xs, tx))

    print(ans)
