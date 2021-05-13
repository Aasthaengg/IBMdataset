import math

sin = math.sin(math.pi/3)
cos = math.cos(math.pi/3)

n = int(input())
p1, p2 = (0, 0), (100, 0)
ans_ls = [p1, p2]

def koch(d, p1, p2):
    if d == n:
        return
    
    s = (2/3 * p1[0] + 1/3 * p2[0], 2/3 * p1[1] + 1/3 * p2[1])
    t = (1/3 * p1[0] + 2/3 * p2[0], 1/3 * p1[1] + 2/3 * p2[1])
    u = ((t[0] - s[0]) * cos - (t[1] - s[1]) * sin + s[0], (t[0] - s[0]) * sin + (t[1] - s[1]) * cos + s[1])
    ans_ls.extend([s, u, t])
    
    koch(d+1, p1, s)
    print(*s)
    koch(d+1, s, u)
    print(*u)
    koch(d+1, u, t)
    print(*t)
    koch(d+1, t, p2)
    
print(*p1)
koch(0, p1, p2)
print(*p2)
