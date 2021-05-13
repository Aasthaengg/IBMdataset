import sys
import bisect
input = sys.stdin.readline

A, B, Q = map(int, input().split())
tera = [int(input()) for _ in range(A)]
sha = [int(input()) for _ in range(B)]
query = [int(input()) for _ in range(Q)]
res = []

for x in query:
    tl = bisect.bisect_left(tera, x)
    tr = bisect.bisect_right(tera, x)
    sl = bisect.bisect_left(sha, x)
    sr = bisect.bisect_right(sha, x)

    if tl == 0:
        temple = [tera[0]]
    elif tr == A:
        temple = [tera[A - 1]]
    else:
        temple = [tera[tl-1], tera[tl]]

    if sl == 0:
        shrine = [sha[0]]
    elif sr == B:
        shrine = [sha[B - 1]]
    else:
        shrine = [sha[sl-1], sha[sl]]

    ans = 10**18
    for t in temple:
        for s in shrine:
            tx = t - x
            sx = s - x
            if tx * sx >= 0:
                a = max(abs(tx), abs(sx))
            else:
                a = min(2 * abs(tx) + abs(sx), 2 * abs(sx) + abs(tx))
            ans = min(ans, a)
    res.append(ans)

print(*res, sep="\n")
