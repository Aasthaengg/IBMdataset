import math

pi = math.pi

n = int(input())
p1 = [0,0]
p2 = [100,0]

def koch(n, p1, p2):
    if n == 0:
        return
    s = [(2*p1[0]+p2[0])/3.0,(2*p1[1]+p2[1])/3.0]
    t = [(1*p1[0]+2*p2[0])/3.0,(p1[1]+2*p2[1])/3.0]
    u = [(t[0]-s[0])*math.cos(pi/3) - (t[1]-s[1])*math.sin(pi/3) + s[0], 
         (t[0]-s[0])*math.sin(pi/3) + (t[1]-s[1])*math.cos(pi/3) + s[1]]
         

    koch(n - 1, p1, s)
    print(*s)
    koch(n - 1, s, u)
    print(*u)
    koch(n - 1, u, t)
    print(*t)
    koch(n - 1, t, p2)

print(*p1)
koch(n, p1, p2)
print(*p2)