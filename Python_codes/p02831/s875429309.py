import fractions
n,m = map(int,input().split())
def lcb(n,m):
    return (n*m)//fractions.gcd(n,m)
    
print(lcb(n,m))