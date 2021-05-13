import fractions

n,k = map(int,input().split())

a = list(map(int,input().split()))

gcd = a[0]

max_a = max(a)

for i in range(1,n):
    gcd = fractions.gcd(gcd,a[i])

if k%gcd==0 and k <= max_a:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')