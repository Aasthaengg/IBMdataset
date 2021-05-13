from fractions import gcd
n,k=map(int,input().split())
*a,=map(int,input().split())

g=a[0]
for i in range(1,n):
    g=gcd(g,a[i])

if k in a or (k%g==0 and k<=max(a)):
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')