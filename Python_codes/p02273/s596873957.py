import math
def kochCurve(A):
    B = []
    for i in xrange(len(A)-1):
        p1 = A[i]
        p2 = A[i+1]
        s = ((A[i][0] * 2.0 + A[i+1][0] * 1.0)/3, (A[i][1] * 2.0 + A[i+1][1] * 1.0)/3)
        t = ((A[i][0] * 1.0 + A[i+1][0] * 2.0)/3, (A[i][1] * 1.0 + A[i+1][1] * 2.0)/3)
        x = t[0] - s[0]
        y = t[1] - s[1]
        rad = math.radians(60)
        ux = x * math.cos(rad) - y * math.sin(rad)
        uy = x * math.sin(rad) + y * math.cos(rad)
        u = (ux + s[0], uy + s[1])
        B.extend([p1, s, u, t])
    B.append(A[len(A)-1])
    return B

n = int(raw_input())
A = [(0, 0), (100, 0)]
for i in xrange(n):
    A = kochCurve(A)
for x in A:
    print x[0], x[1]