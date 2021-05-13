import math

class KochCurve:
    def koch(self, d, p1, p2): 
        if d == 0:
            return
        th = math.pi * 60.0 / 180.0
        sx = (2.0 * p1[0] + 1.0 * p2[0]) / 3
        sy = (2.0 * p1[1] + 1.0 * p2[1]) / 3
        s = [sx, sy]
        tx = (1.0 * p1[0] + 2.0 * p2[0]) / 3
        ty = (1.0 * p1[1] + 2.0 * p2[1]) / 3
        t = [tx, ty]
        ux = (tx - sx) * math.cos(th) - (ty - sy) * math.sin(th) + sx
        uy = (tx - sx) * math.sin(th) + (ty - sy) * math.cos(th) + sy
        u = [ux, uy]
        
        self.koch(d-1, p1, s)
        print("{} {}".format(sx, sy))
        
        self.koch(d-1, s, u)
        print("{} {}".format(ux, uy))

        self.koch(d-1, u, t)
        print("{} {}".format(tx, ty))
        
        self.koch(d-1, t, p2)

if __name__ == '__main__':
    n = int(input().rstrip())
    p1 = [0, 0]
    p2 = [100, 0]
    print("{} {}".format(p1[0], p1[1]))
    x = KochCurve()
    x.koch(n, p1, p2)
    print("{} {}".format(p2[0], p2[1]))