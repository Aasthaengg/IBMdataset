import math

pi=math.pi

def Koch(n,p0,p1):
        if n==0:
           return False

        s=[0 for i in range(2)]
        t=[0 for i in range(2)]
        u=[0 for i in range(2)]
        
        s =[(2*p0[0]+1*p1[0])/3.0,(2*p0[1]+1*p1[1])/3.0]
        t =[(1*p0[0]+2*p1[0])/3.0,(1*p0[1]+2*p1[1])/3.0]
        u =[(t[0]-s[0]) * math.cos (pi / 3) - (t[1]-s[1])* math.sin (pi / 3)+s[0],(t[0]-s[0]) * math.sin (pi / 3) + (t[1]-s[1])* math.cos (pi / 3)+s[1]]
        Koch(n-1,p0,s)
        print("{0:.8f} {1:.8f}".format(s[0],s[1]))
        Koch(n-1,s,u)
        print("{0:.8f} {1:.8f}".format(u[0],u[1]))
        Koch(n-1,u,t)
        print("{0:.8f} {1:.8f}".format(t[0],t[1]))
        Koch(n-1,t,p1)

p0=[0, 0]
p1=[100,0]
n=int(input())

print("{0:.8f} {1:.8f}".format(p0[0],p0[1]))
Koch(n,p0,p1)
print("{0:.8f} {1:.8f}".format(p1[0],p1[1]))

