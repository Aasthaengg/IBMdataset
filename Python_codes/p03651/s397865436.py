def f(a,b):
    if b:return f(b,a%b)
    return a
n,k=map(int,input().split())
a=list(map(int,input().split()))
if n==1:
    print('POSSIBLE' if k==a[0] else 'IMPOSSIBLE')
    exit()
p=f(a[0],a[1])
for i in a[1:]:
    p=f(p,i)
print('POSSIBLE' if p==f(p,k) and k<=max(a) else 'IMPOSSIBLE')