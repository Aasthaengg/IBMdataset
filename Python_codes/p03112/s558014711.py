a, b, q = map(int, input().split())
S = [int(input()) for _ in range(a)]
T = [int(input()) for _ in range(b)]
S.sort()
T.sort()
INF = 10**18
S = [-INF] + S + [INF]
T = [-INF] + T + [INF]

import bisect
for _ in range(q):
    x = int(input())
    i = bisect.bisect_right(S, x)
    j = bisect.bisect_right(T, x)
    ans = INF
    for s in [S[i-1], S[i]]:
        for t in [T[j-1], T[j]]:
            d1 = abs(s-x) + abs(t-s)
            d2 = abs(t-x) + abs(s-t)
            ans = min([ans, d1, d2])
    print(ans)