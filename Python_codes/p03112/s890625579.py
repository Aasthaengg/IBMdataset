A,B,Q = map(int, input().split())
S = [int(input()) for _ in range(A)]
T = [int(input()) for _ in range(B)]
import bisect
for _ in range(Q):
    x = int(input())
    s_idx = bisect.bisect_left(S, x)
    t_idx = bisect.bisect_left(T, x)
    if s_idx == A and t_idx == B:
        ans = x-min(S[-1], T[-1])
    elif s_idx == A and t_idx == 0:
        ans = min(x-S[-1]*2+T[0], T[0]*2-x-S[-1])
    elif t_idx == B and s_idx == 0:
        ans = min(x-T[-1]*2+S[0], S[0]*2-x-T[-1])
    elif s_idx == A:
        ans = min(x-min(S[-1], T[t_idx-1]), x-S[-1]*2+T[t_idx], T[t_idx]*2-x-S[-1])
    elif t_idx == B:
        ans = min(x-min(T[-1], S[s_idx-1]), x-T[-1]*2+S[s_idx], S[s_idx]*2-x-T[-1])
    elif s_idx == 0 and t_idx == 0:
        ans = max(S[0], T[0])-x
    elif s_idx == 0:
        ans = min(max(S[0], T[t_idx])-x, S[0]*2-x-T[t_idx-1], x-T[t_idx-1]*2+S[0])
    elif t_idx == 0:
        ans = min(max(T[0], S[s_idx])-x, T[0]*2-x-S[s_idx-1], x-S[s_idx-1]*2+T[0])
    else:
        ans = min(max(S[s_idx], T[t_idx])-x, x-min(S[s_idx-1], T[t_idx-1]), S[s_idx]*2-x-T[t_idx-1], T[t_idx]*2-x-S[s_idx-1])
        ans = min(ans, x-T[t_idx-1]*2+S[s_idx], x-S[s_idx-1]*2+T[t_idx])
    print(ans)