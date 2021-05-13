import math

def kochCurve(p1, p2, n):
    if n == 0:
        print "%5f %5f" % (p2[0], p2[1])
        return

    s = ((p2[0] - p1[0]) / 3.0 + p1[0], (p2[1] - p1[1]) / 3.0 + p1[1])
    t = ((p2[0] - p1[0]) * 2.0 / 3 + p1[0], (p2[1] - p1[1]) * 2.0 / 3 + p1[1])
    u = (math.cos(math.pi/3)*(t[0]-s[0])-math.sin(math.pi/3)*(t[1]-s[1])+s[0], math.sin(math.pi/3)*(t[0]-s[0])+math.cos(math.pi/3)*(t[1]-s[1])+s[1])

    kochCurve(p1, s, n - 1)
    kochCurve(s, u, n - 1)
    kochCurve(u, t, n - 1)
    kochCurve(t, p2, n - 1)

if __name__ == "__main__":
    n = int(input())
    p1 = (0, 0)
    p2 = (100, 0)
    print "%5f %5f" % (p1[0], p1[1])
    kochCurve(p1, p2, n)