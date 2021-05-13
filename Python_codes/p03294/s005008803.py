n=int(input())
a=list(map(int, input().split()))
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a,b):
    return a*b//gcd(a,b)
x=1
for t in a:
    x=lcm(x,t)
x-=1
ans=0
for t in a:
    ans+=x%t
print(ans)
