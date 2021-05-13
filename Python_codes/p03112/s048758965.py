a, b, q = map(int, input().split())
S = [int(input()) for _ in range(a)]
T = [int(input()) for _ in range(b)]

S.sort()
T.sort()

S = [-10**18]+S+[10**18]
T = [-10**18]+T+[10**18]

import bisect

for i in range(q):
    x = int(input())
    j = bisect.bisect_left(S, x)
    k = bisect.bisect_left(T, x)
    ans = 10**18
    for dj, dk in (-1, -1), (-1, 0), (0, -1), (0, 0):
        nj = j+dj
        nk = k+dk
        temp = min(abs(S[nj]-x)+abs(T[nk]-S[nj]), abs(T[nk]-x)+abs(T[nk]-S[nj]))
        ans = min(ans, temp)
    print(ans)
