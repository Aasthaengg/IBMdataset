# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_C
# Koch Curve
# Result:
import sys
import math

# 60 degree
degree = math.pi / 3

def print_point(point):
    print '%f %f' % (point[0], point[1])

def koch(depth, p1, p2):
    if depth == 0:
        return
    s = ((2 * p1[0] + p2[0]) / 3, (2 * p1[1] + p2[1]) / 3)
    t = ((p1[0] + 2 * p2[0]) / 3, (p1[1] + 2 * p2[1]) / 3)
    u = ((t[0] - s[0]) * math.cos(degree) - (t[1] - s[1]) * math.sin(degree) + s[0],
         (t[0] - s[0]) * math.sin(degree) + (t[1] - s[1]) * math.cos(degree) + s[1])
    depth -= 1
    koch(depth, p1, s)
    print_point(s)
    koch(depth, s, u)
    print_point(u)
    koch(depth, u, t)
    print_point(t)
    koch(depth, t, p2)

n_itr = int(sys.stdin.readline())
start = (0.0, 0.0)
end = (100.0, 0.0)
print_point(start)
koch(n_itr, start, end)
print_point(end)