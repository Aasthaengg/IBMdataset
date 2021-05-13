A, B, C, D = map(int,input().split())
c = B//C-A//C + (A%C == 0)
d = B//D-A//D + (A%D == 0)
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)
def lcm(a,b):
    return a*b//gcd(a,b)
E = lcm(C,D)
e = B//E-A//E + (A%E == 0)
print(B-A+1-c-d+e)
