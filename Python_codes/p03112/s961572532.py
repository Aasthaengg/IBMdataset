import bisect
a, b, q = map(int, input().split())
s = [int(input()) for _i in range(a)]
t = [int(input()) for _i in range(b)]
s.append(float('inf'))
s.insert(0, -float('inf'))
t.append(float('inf'))
t.insert(0, -float('inf'))
x = [int(input()) for _i in range(q)]

for i in x:
    n = bisect.bisect_right(s, i)
    m = bisect.bisect_right(t, i)
    e = abs(max([s[n], t[m]])-i)
    f = abs(i-min(s[n-1], t[m-1]))
    g = min([abs(i-s[n]), abs(i-t[m-1])])+abs(s[n]-t[m-1])
    h = min([abs(i-s[n-1]), abs(i-t[m])])+abs(s[n-1]-t[m])
    print(min([e, f, g, h]))