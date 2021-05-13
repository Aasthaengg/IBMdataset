import fractions
import functools
n=int(input())
a=list(map(int,input().split()))
tmp=1
for f in a:
    tmp*=f
gcd=functools.reduce(fractions.gcd, a)
lcm=tmp//gcd
lcm-=1
ans=0
for f in a:
    ans+=lcm%f
print(ans)