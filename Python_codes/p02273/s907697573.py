import math

def koch(a1, a2, b1, b2, n):
    if n <= 0:
        return 0

    s1 = 2.0/3.0*a1 + 1.0/3.0*b1
    s2 = 2.0/3.0*a2 + 1.0/3.0*b2
    t1 = 1.0/3.0*a1 + 2.0/3.0*b1
    t2 = 1.0/3.0*a2 + 2.0/3.0*b2
    u1 = 1.0/6.0*(3.0*a1 + 3.0*b1 + math.sqrt(3.0)*a2 - math.sqrt(3.0)*b2)
    u2 = 1.0/6.0*(-1.0*math.sqrt(3.0)*a1 + math.sqrt(3.0)*b1 + 3.0*a2 + 3.0*b2)
    
    koch(a1, a2, s1, s2, n-1)
    print s1, s2
    koch(s1, s2, u1, u2, n-1)
    print u1, u2
    koch(u1, u2, t1, t2, n-1)
    print t1, t2
    koch(t1, t2, b1, b2, n-1)
    
if __name__ == '__main__':
    n = int(raw_input())
    a1, a2, b1, b2 = 0.0, 0.0, 100.0, 0.0
    print a1, a2
    koch(a1, a2, b1, b2, n)
    print b1, b2