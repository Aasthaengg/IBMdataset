n,m=map(int,input().split())
s=str(input())
t=str(input())
def gcd(x, y):
    if x % y == 0:
        return(y)
    else:
        return gcd(y,x%y)
def lcm(a,b):
    return a*b//gcd(a,b)
a=n//gcd(n,m)
b=m//gcd(n,m)
for i in range(gcd(n,m)):
    if s[a*i]!=t[b*i]:
        print("-1")
        exit()
print(lcm(n,m))