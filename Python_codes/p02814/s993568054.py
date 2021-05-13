from fractions import gcd

n,m = map(int,input().split())
a = set(map(int,input().split()))
a = list(a)
nn = len(a)

g = a[0]
    
x = a[0]
for i in range(1,nn):
    t = gcd(x,a[i])
    x *= a[i]
    x //= t
    
fl = 1
ff = x//2
for i in range(nn):
    if ff % a[i] != a[i] // 2:
        fl = 0
        
if fl == 1:
    xx = (m-ff) // x + 1
else:
    xx = 0
    
print(xx)