from collections import deque

X, Y, A, B, C = map(int, input().split())
p = sorted(list(map(int, input().split())), reverse=True)
q = sorted(list(map(int, input().split())), reverse=True)
r = sorted(list(map(int, input().split())), reverse=True)

p = deque(p)
q = deque(q)
r = deque(r)

ans = 0
MIN = -1
N = X + Y
for _ in range(N):
    tmp_p, tmp_q, tmp_r = MIN, MIN, MIN
    if len(p) > 0 and X > 0:
        tmp_p = p.popleft()
    if len(q) > 0 and Y > 0:
        tmp_q = q.popleft()
    if len(r) > 0:
        tmp_r = r.popleft()
    
    if tmp_p >= tmp_q and tmp_p >= tmp_r:
        ans += tmp_p
        X -= 1
        if tmp_q != -1:
            q.appendleft(tmp_q)
        if tmp_r != -1:
            r.appendleft(tmp_r)

    elif tmp_q >= tmp_p and tmp_q >= tmp_r:
        ans += tmp_q
        Y -= 1
        if tmp_p != -1:
            p.appendleft(tmp_p)
        if tmp_r != -1:
            r.appendleft(tmp_r)

    else:
        ans += tmp_r
        if tmp_q != -1:
            q.appendleft(tmp_q)
        if tmp_p != -1:
            p.appendleft(tmp_p)

print(ans)
