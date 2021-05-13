from math import pi,sin,cos

def print_p(p):
    print("{0:.8f} {1:.8f}".format(*p))

def koch(n,p1,p2):
    if n==0: return
    s = tuple(map(lambda z: (2*z[0]+  z[1])/3, zip(p1,p2)))
    t = tuple(map(lambda z: (  z[0]+2*z[1])/3, zip(p1,p2)))
    u = ( (t[0]-s[0])*cos(60*(pi/180)) - (t[1]-s[1])*sin(60*(pi/180)) + s[0] \
         ,(t[0]-s[0])*sin(60*(pi/180)) + (t[1]-s[1])*cos(60*(pi/180)) + s[1] )
    koch(n-1,p1,s)
    print_p(s)
    koch(n-1,s,u)
    print_p(u)
    koch(n-1,u,t)
    print_p(t)
    koch(n-1,t,p2)

if __name__=='__main__':
    n=int(input()) 
    p1 = [0.0  , 0.0]
    p2 = [100.0, 0.0]
    print_p(p1)
    koch(n,p1,p2)
    print_p(p2)