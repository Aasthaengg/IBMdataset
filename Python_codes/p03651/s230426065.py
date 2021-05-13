N,K=map(int, input().split())
*A,=map(int, input().split())
def gcd(a,b):
    while b: a,b=b,a%b
    return a
g=0
for a in A: g=gcd(g,a)
print('POSSIBLE' if K%g==0 and K<=max(A) else 'IMPOSSIBLE')