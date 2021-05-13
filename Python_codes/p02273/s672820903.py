
def vector_u(vc_p1 = [], vc_p2 = []):
    vc_p1s = [(vc_p2[0] - vc_p1[0])/3.0, (vc_p2[1] - vc_p1[1])/3.0]
    vc_su  = [vc_p1s[0]*0.5 - vc_p1s[1]*0.866025, vc_p1s[0]*0.866025 + vc_p1s[1]*0.5]
    vc_u   = [vc_p1[0] + vc_p1s[0] + vc_su[0], vc_p1[1] + vc_p1s[1] + vc_su[1]]
    return vc_u

def vector_s(vc_p1 = [], vc_p2 = []):
    vc_s = [(2.0*vc_p1[0] + vc_p2[0])/3.0, (2.0*vc_p1[1] + vc_p2[1])/3.0]
    return vc_s

def vector_t(vc_p1 = [], vc_p2 = []):
    vc_t = [(vc_p1[0] + 2.0*vc_p2[0])/3.0, (vc_p1[1] + 2.0*vc_p2[1])/3.0]
    return vc_t

def koch_curve(p1 = [0.00000, 0.00000], p2 = [100.00000, 0.00000], n = 0):
    s = vector_s(p1, p2)
    u = vector_u(p1, p2)
    t = vector_t(p1, p2)
    
    if n == 0:
        print(str( s[0]) + " " + str( s[1]))
        print(str( u[0]) + " " + str( u[1]))
        print(str( t[0]) + " " + str( t[1]))
        print(str(p2[0]) + " " + str(p2[1]))
    else:
        koch_curve(p1,  s, n-1)
        koch_curve( s,  u, n-1)
        koch_curve( u,  t, n-1)
        koch_curve( t, p2, n-1)

n = int(raw_input())

p1 = [  0.0, 0.0]
p2 = [100.0, 0.0]

print(str(p1[0]) + " " + str(p1[1]))
if n == 0:
    print(str(p2[0]) + " " + str(p2[1]))
else:
    koch_curve(p1, p2, n-1)