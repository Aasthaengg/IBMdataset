from bisect import bisect_left, bisect, bisect_right
a, b, q = map(int, input().split())
INF = 10 ** 18
S = [-INF] + [int(input()) for _ in range(a)] + [INF]
T = [-INF] + [int(input()) for _ in range(b)] + [INF]
start = [int(input()) for _ in range(q)]

for now_start in start:
    s_id = bisect_left(S, now_start)
    t_id = bisect_left(T, now_start)
    dist1 = abs(now_start - min(S[s_id - 1], T[t_id - 1]))
    dist2 = abs(now_start - max(S[s_id], T[t_id]))
    if max(S[s_id - 1], T[t_id - 1]) == S[s_id - 1]:
        dist3 = abs(now_start - S[s_id - 1]) + abs(T[t_id] - S[s_id - 1])
    elif max(S[s_id - 1], T[t_id - 1]) == T[t_id - 1]:
        dist3 = abs(now_start - T[t_id - 1]) + abs(S[s_id] - T[t_id - 1])
    if min(S[s_id], T[t_id]) == S[s_id]:
        dist4 = abs(now_start - S[s_id]) + abs(T[t_id - 1] - S[s_id])
    elif min(S[s_id], T[t_id]) == T[t_id]:
        dist4 = abs(now_start - T[t_id]) + abs(S[s_id - 1] - T[t_id])
    print(min(dist1, dist2, dist3, dist4))