from operator import itemgetter
import sys

input = sys.stdin.readline

inf = float('inf')

N, Q = map(int, input().split())

events = []
method_events_append = events.append

for _ in range(N):
    s, t, x = map(int, input().split())
    method_events_append((s - x, 1, x))  # add_event
    method_events_append((t - x, -1, x))  # remove_event

events.sort(key=itemgetter(0))  # イベント処理時刻昇順ソート

under_construction = set()
method_uc_add = under_construction.add
method_uc_discard = under_construction.discard

min_stop = inf
not_chg_flg = True

cur = 0
for _ in range(Q):
    d = int(input())
    while cur < N * 2 and events[cur][0] <= d:
        exec_time, event_type, under_construction_x = events[cur]
        if event_type == 1:  # add_event
            method_uc_add(under_construction_x)
            if not_chg_flg:  # この分岐がないとdiscardされたmin_stopと比較する恐れがある
                min_stop = min(min_stop, under_construction_x)
        else:  # remove_event
            method_uc_discard(under_construction_x)
            if not_chg_flg and min_stop == under_construction_x:
                not_chg_flg = False
        cur += 1

    if not not_chg_flg:
        min_stop = min(under_construction) if under_construction else inf
        not_chg_flg = True
    print(min_stop if min_stop != inf else -1)
