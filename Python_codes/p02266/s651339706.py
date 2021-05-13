from collections import deque
S = input()
d = deque()
d2 = deque()
r = []
r_l = 0
buf = 0
for i, s in enumerate(S):
    i += 1
    if s == '\\':
        d.append(i)
    elif s == '/' and len(d) > 0:
        k = d.pop()
        r_l += i - k
        buf = i - k
        while(len(d2) > 0 and d2[-1][0] > k):
            _d = d2.pop()
            buf += _d[1]
        l = [k, buf]
        d2.append(l)

r = []
for i in d2:
    r.append(i[1])
print(r_l)
print(len(r), *r)

