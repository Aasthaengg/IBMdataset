n,m=map(int,input().split())
s=input()
t=input()

from fractions import gcd
def lcm(a):
    x = a[0]
    for i in range(1, len(a)):
        x = (x * a[i]) // gcd(x, a[i])
    return x

long=lcm([n,m])

ln=int(long/n)
lm=int(long/m)

#ans=[]

ok=True

for i in range(n-1):
    if (i*ln)%lm==0:
        if s[i]!=t[(i*ln)//lm]:
            ok=False

if n==1:
    if s!=t[0]:ok=False
if m==1:
    if t!=s[0]:ok=False

if not ok:long=-1

print(long)