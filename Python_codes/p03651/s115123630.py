from math import gcd

n,k = map(int,input().split())
a = list(map(int,input().split()))

gcd_num = a[0]
for ai in a[1:]:
    gcd_num = gcd(gcd_num,ai)

if(k%gcd_num==0)&(k <= max(a)):
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')