from operator import itemgetter
import sys

input = sys.stdin.readline
inf = float('inf')

n, q = map(int, input().split())

e = []
for _ in range(n):
    s, t, x = map(int, input().split())
    # 区間[s, t)に通行止め
    e.append((s - x, x, 0))  # 通行止め開始
    e.append((t - x - 0.5, x, 1))  # 通行止め解除
e.sort(key=itemgetter(0))

stop_set = set()
stop_at = inf
cur = 0
for _ in range(q):
    changed = False
    d = int(input())
    while cur < n * 2:
        exec_time, pos, typ = e[cur]
        if exec_time <= d:
            if typ == 0:
                stop_set.add(pos)
                if (not changed) and (pos < stop_at):
                    stop_at = pos
            else:
                stop_set.remove(pos)
                if (not changed) and (pos == stop_at):
                    changed = True
            cur += 1
        else:
            break

    if changed:
        if stop_set:
            stop_at = min(stop_set)
        else:
            stop_at = inf

    print(stop_at if stop_at != inf else -1)
