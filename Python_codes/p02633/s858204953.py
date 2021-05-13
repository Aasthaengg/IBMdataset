def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

x=int(input())
print(360//(gcd(360,x)))