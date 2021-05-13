import sys
def gcd(a,b):
    if a==b:
        return a
    while(b>0):
        a,b = b,a%b
        if b==0:
            return a
def lcm(a,b):
    n=1
    m=1
    while(n*a!=m*b):
        if n*a>m*b:
            m+=1
        elif n*a<m*b:
            n+=1
    return n*a
lines = sys.stdin.readlines()
for line in lines:
    line = line.split(" ")
    inp = []
    for i in line:
        inp.append(int(i))
    inp.sort()
    a = inp[0]
    b = inp[1]
    print("%d %d" % (gcd(a,b),lcm(a,b)))