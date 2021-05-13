import math

n = int(input())

def koch(n,a,b): #a,b:tuple
    if n==0:
        return
    th = math.pi*60/180
    s = ((2*a[0]+b[0])/3,(2*a[1]+b[1])/3)
    t = ((a[0]+2*b[0])/3,(a[1]+2*b[1])/3)
    u = ((t[0]-s[0])*math.cos(th)-(t[1]-s[1])*math.sin(th)+s[0],(t[0]-s[0])*math.sin(th)+(t[1]-s[1])*math.cos(th)+s[1])

    koch(n-1,a,s)
    print(s[0],s[1])
    koch(n-1,s,u)
    print(u[0],u[1])
    koch(n-1,u,t)
    print(t[0],t[1])
    koch(n-1,t,b)

a = (0,0)
b = (100,0)
print(a[0],a[1])
koch(n,a,b)
print(b[0],b[1])
