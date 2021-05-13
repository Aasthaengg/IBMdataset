from operator import itemgetter
import sys

input = sys.stdin.readline

inf = float('inf')

N, Q = map(int, input().split())

es = []
for _ in range(N):
    s, t, x = map(int, input().split())
    es.append((s - x, 1, x))
    es.append((t - x - 0.5, -1, x))

es.sort(key=itemgetter(0))
st = set()
cur_min_stop = inf
check_needed = True

# print(es)
i = 0
for _ in range(Q):
    d = int(input())
    while i < N * 2:
        time, typ, pos = es[i]
        # print(es[i])
        if time > d:
            break
        if typ == 1:
            st.add(pos)
            if pos < cur_min_stop:
                cur_min_stop = pos
        else:
            st.remove(pos)
            if pos == cur_min_stop:
                check_needed = True
        i = i + 1

    if check_needed:
        if st:
            cur_min_stop = min(st)
        else:
            cur_min_stop = inf
        check_needed = False
    print(cur_min_stop if cur_min_stop < inf else -1)
