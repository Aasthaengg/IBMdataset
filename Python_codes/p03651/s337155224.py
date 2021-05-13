import fractions
n,k=map(int,input().split())
a=sorted(list(map(int,input().split())))
b=[0]*n
if k>max(a):
    print("IMPOSSIBLE")
    exit()
g=a[0]
for i in range(1,n):
    g=fractions.gcd(g,a[i])
for i in range(n):
    b[i]=a[i]%g
if k%g in b:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")