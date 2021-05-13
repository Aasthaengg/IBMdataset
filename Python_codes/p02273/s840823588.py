import math

def make_3_points(p1, p2):
    """p1, p2 を分割する３点を作成する。
    
    p1, p2 を両端の点とする線分を３等分する２点 s, t を
    頂点とする正三角形の頂点 (s, u, t) のタプルを返す。
    """
    s = ((2 * p1[0] + p2[0]) / 3, (2 * p1[1] + p2[1]) / 3)
    t = ((p1[0] + 2 * p2[0]) / 3, (p1[1] + 2 * p2[1]) / 3)

    theta = math.radians(60)

    x = t[0] - s[0]
    y = t[1] - s[1]

    u = (math.cos(theta) * x - math.sin(theta) * y, math.sin(theta) * x + math.cos(theta) * y)
    u = (u[0] + s[0], u[1] + s[1])

    return (s, u, t)

def make_koch(n, pl):
    if n == 0:
        return pl
    next_pl = [pl[0]]
    for i in range(1, len(pl)):
        s, u, t = make_3_points(next_pl[-1], pl[i])
        next_pl += [s, u, t, pl[i]]
    
    pl = None
    return make_koch(n - 1, next_pl)

n = int(input())
rl = make_koch(n, [(0, 0), (100, 0)])
for p1, p2 in rl:
    print(p1, p2)

