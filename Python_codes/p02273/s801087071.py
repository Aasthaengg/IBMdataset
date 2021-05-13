import math

n = int(input())

def dividing_point(p1, p2, ratio):
    return ( p1[0]*(1-ratio) + p2[0]*ratio, p1[1]*(1-ratio) + p2[1]*ratio)

def rotate_vec_60deg(v):
    return (v[0]/2 - math.sqrt(3)*v[1]/2, math.sqrt(3)*v[0]/2 + v[1]/2)
    

def koch(depth, p_left, p_right):
    if depth == 0:
        return
    
    s = dividing_point(p_left, p_right, 1/3)
    t = dividing_point(p_left, p_right, 2/3)
    tmpvec = rotate_vec_60deg((s[0] - p_left[0], s[1] - p_left[1] ))
    u = (s[0] + tmpvec[0], s[1] + tmpvec[1])
    
    koch(depth - 1, p_left, s)
    print(s[0], s[1])
    koch(depth - 1, s, u)
    print(u[0], u[1])
    koch(depth - 1, u, t)
    print(t[0], t[1])
    koch(depth - 1, t, p_right)
    
    
print(0.0, 0.0)
koch(n, (0,0), (100, 0))
print(100.0, 0)
