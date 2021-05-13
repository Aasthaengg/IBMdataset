import bisect

a, b, q = map(int, input().split())
s = [int(input()) for _ in range(a)]
t = [int(input()) for _ in range(b)]
x = [int(input()) for _ in range(q)]
inf = pow(10, 12)
s.insert(0, -inf)
s.append(inf)
t.insert(0, -inf)
t.append(inf)
for i in x:
    u, v = bisect.bisect_left(s, i), bisect.bisect_left(t, i)
    s1, s2 = s[u - 1], s[u]
    t1, t2 = t[v - 1], t[v]
    d1 = max(i - s1, i - t1)
    d2 = max(s2 - i, t2 - i)
    d3 = max(i - s1, t2 - i) + 2 * min(i - s1, t2 - i)
    d4 = max(i - t1, s2 - i) + 2 * min(i - t1, s2 - i)
    print(min(d1, d2, d3, d4))