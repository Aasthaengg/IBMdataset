def gcd(a,b):
    x=max(a,b)
    y=min(a,b)
    if x%y==0:
        return y
    else:
        while x%y!=0:
            z=x%y
            x=y
            y=z
        else:
            return z
        
def lcm(a,b):
    return int(a*b//gcd(a,b))

N=int(input())

a=int(input())

for n in range(1,N):
    b=int(input())
    a=lcm(a,b)
print(a)