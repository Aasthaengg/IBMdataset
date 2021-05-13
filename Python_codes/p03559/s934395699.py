import bisect
n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]
a.sort()
b.sort()
c.sort()
s = 0
for b_ in b:
    t = bisect.bisect_right(a, b_-1)
    tt = len(c) - bisect.bisect_right(c, b_)
    d = tt * t
    s += d
print(s)