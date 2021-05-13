def gcd(a,b):
    if b==0: return a
    return gcd(b,a%b)
a,b,c = map(int,input().split())
print('YES' if c%gcd(a,b)==0 else 'NO')