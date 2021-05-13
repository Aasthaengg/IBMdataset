import sys
input = sys.stdin.readline


n, q = map(int, input().split())
events = []
for _ in range(n):
    start, end, pos = map(int, input().split())
    events.append([start - pos, 1, pos])
    events.append([end - pos, 0, pos])

events.sort()

departures = [int(input()) for _ in range(q)]

idx = 0
mini = 10**10
mini_check = False
candidates = set()
time, is_under_construction, pos = events[idx]
for departure in departures:
    while time <= departure:
        if is_under_construction:
            candidates.add(pos)
            if pos < mini:
                mini = pos
                mini_check = True
        else:
            candidates.remove(pos)
            if pos == mini:
                mini_check = False
        idx += 1
        if idx == 2 * n:
            time = float('INF')
            break
        time, is_under_construction, pos = events[idx]

    if not candidates:
        print(-1)
    else:
        if not mini_check:
            mini = min(candidates)
            mini_check = True
        print(mini)
