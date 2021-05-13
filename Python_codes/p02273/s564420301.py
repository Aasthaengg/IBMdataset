import math

def koch(n, p1, p2):
    if n == 0:
        return False

    #p1, p2??????s, t, u????¨????
    s = [0 for i in range(2)]
    t = [0 for i in range(2)]
    u = [0 for i in range(2)]
    s[0] = (2*p1[0] + 1*p2[0]) / 3
    s[1] = (2*p1[1] + 1*p2[1]) / 3
    t[0] = (1*p1[0] + 2*p2[0]) / 3
    t[1] = (1*p1[1] + 2*p2[1]) / 3
    u[0] = (t[0]-s[0]) * math.cos(60 * math.pi / 180) - (t[1]-s[1]) * math.sin(60 * math.pi / 180) + s[0]
    u[1] = (t[0]-s[0]) * math.sin(60 * math.pi / 180) + (t[1]-s[1]) * math.cos(60 * math.pi / 180) + s[1]

    koch(n-1, p1, s)
    print(*s)
    koch(n-1, s, u)
    print(*u)
    koch(n-1, u, t)
    print(*t)
    koch(n-1, t, p2)

p1 = [0, 0]
p2 = [100,0]
n = int(input())
print("0.00000 0.00000")
koch(n, p1, p2)
print("100.0000 0.0000")