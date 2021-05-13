import math


def koch(p1, p2, count):
    """Find points in koch curve after count times operations.

    >>> ps = koch((0, 0), (100, 0), 1)
    >>> cs = ["({:.4f}, {:.4f})".format(*p) for p in ps]
    >>> print("\\n".join(cs))
    (0.0000, 0.0000)
    (33.3333, 0.0000)
    (50.0000, 28.8675)
    (66.6667, 0.0000)
    (100.0000, 0.0000)
    """

    if count == 0:
        return []

    (x1, y1) = p1
    (x2, y2) = p2

    r, t = cartesian_to_polar(x2-x1, y2-y1)

    x3, y3 = polar_to_cartesian(r/3, t)
    p3 = (x3+x1, y3+y1)

    x4, y4 = polar_to_cartesian(r / (2*math.cos(math.pi/6)), t + math.pi/6)
    p4 = (x4+x1, y4+y1)

    x5, y5 = polar_to_cartesian(2*r/3, t)
    p5 = (x5+x1, y5+y1)

    return (koch(p1, p3, count-1)
            + [p3] + koch(p3, p4, count-1)
            + [p4] + koch(p4, p5, count-1)
            + [p5] + koch(p5, p2, count-1))


def polar_to_cartesian(x, y):
    return (x * math.cos(y), x * math.sin(y))


def cartesian_to_polar(x, y):
    return (math.sqrt(x**2 + y**2), math.atan2(y, x))


def run():
    n = int(input())
    p1 = (0.0, 0.0)
    p2 = (100.0, 0.0)
    ps = [p1] + koch(p1, p2, n) + [p2]

    # plot(ps)
    print("\n".join(["{:.5f} {:.5f}".format(*p) for p in ps]))


def plot(ps):
    import pylab
    xs = [x for x, y in ps]
    ys = [y for x, y in ps]

    pylab.plot(xs, ys)
    pylab.xlim(0, 100)
    pylab.ylim(0, 100)
    pylab.show()


if __name__ == '__main__':
    run()

