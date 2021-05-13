# AtCoder Beginner Contest 111
# C - /\/\/\/
# https://atcoder.jp/contests/abc111/tasks/arc103_a
from collections import Counter

N, *A = map(int, open(0).read().split())

ev = A[0::2]
od = A[1::2]

ev_C = Counter(ev)
od_C = Counter(od)


if ev == od and ev_C.most_common()[0][1] == N//2:
    print(N//2)
else:
    ans = N
    ev_common = ev_C.most_common()
    od_common = od_C.most_common()
    ev_most = ev_common[0][1]
    od_most = od_common[0][1]
    if ev_common[0][0] == od_common[0][0]:
        ev_second = ev_common[1][1]
        od_second = od_common[1][1]
        ans = min(ans, N-ev_most-od_second)
        ans = min(ans, N-ev_second-od_most)
    else:
        ans = min(ans, N-ev_most-od_most)

    print(ans)
