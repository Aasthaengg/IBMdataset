from bisect import *
A,B,Q=map(int,input().split())
s = [int(input()) for _ in range(A)]
t = [int(input()) for _ in range(B)]
st = [] # (z, 0or1)0ならs, 1ならt
for i in range(A):
    st.append((s[i], 0))
for i in range(B):
    st.append((t[i], 1))

st.sort(key=lambda x: x[0])
INF = float("inf")

for _ in range(Q):
    x = int(input())
    b_left = bisect_left(st, (x, 0))
    ids = [b_left-1, b_left, b_left+1]
    dists = []
    for idx in ids:
        if 0 <= idx <= A+B-1:
            dists.append((abs(x - st[idx][0]), idx))

    ans = INF
    for start in dists:
        tmp = start[0]
        s_idx = start[1]
        now = st[s_idx][0]
        if st[s_idx][1] == 0: #s
            t_left = bisect_left(t, now)
            additional = []
            for nxt in [t_left-1, t_left, t_left+1]:
                if 0<=nxt<=B-1:
                    additional.append(abs(now - t[nxt]))
            delta = min(additional)
            ans = min(ans, tmp+delta)
        else:
            s_left = bisect_left(s, now)
            additional = []
            for nxt in [s_left-1, s_left, s_left+1]:
                if 0 <= nxt <= A-1:
                    additional.append(abs(now - s[nxt]))
            delta = min(additional)
            ans = min(ans, tmp+delta)
    print(ans)