n, k, c = map(int, input().split())
s = list(input())
# cnt = s.count('o')
os = [i for i,x in enumerate(s) if x=='o']

from collections import deque

q = deque(os.copy())
_q1 = q.popleft()
m = k-1
l = [_q1]
if m > 0:
    while q:
        _q2 = q.popleft()
        if _q2 - _q1 > c:
            l.append(_q2)
            _q1 = _q2
            m -= 1
            if m == 0:
                q = deque([])
        else:
            pass

q = deque(os.copy())
_q2 = q.pop()
m = k-1
r = [_q2]
if m > 0:
    while q:
        _q1 = q.pop()
        if _q2 - _q1 > c:
            r.append(_q1)
            _q2 = _q1
            m -= 1
            if m == 0:
                q = deque([])
        else:
            pass

r = list(reversed(r))

ans = 0
for _l, _r in zip(l, r):
    if _l == _r:
        print(str(_l+1))
        ans = 1

if ans == 0:
    print()
