n,k=map(int,input().split())
a=list(map(int,input().split()))
if k> max(a):
    print('IMPOSSIBLE')
    exit()
import fractions
b=a[0]
for i in range(1,n):
    b=fractions.gcd(b,a[i])
print('POSSIBLE' if k%b==0 else 'IMPOSSIBLE')
