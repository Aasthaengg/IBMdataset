from fractions import gcd
N=int(input())
def lcm(a,b):
    return a//gcd(a,b)*b
T=[]
for i in range(N):
    t=int(input())
    T.append(t)
a=1
for i in range(N):
    a=lcm(a,T[i])

print(a)