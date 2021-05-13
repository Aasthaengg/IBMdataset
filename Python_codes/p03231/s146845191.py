from fractions import gcd
def lcm(x,y):
    return x*y//gcd(x,y)
n,m = map(int,input().split())
s=input()
t=input()

l=lcm(n,m)
x=dict()

for i in range(n):
    x[i*(l//n)]=s[i]

for i in range(m):
    j=i*(l//m)
    if j in x and x[j]!=t[i]:
        print(-1)
        exit()
print(l)
