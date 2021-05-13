def gcd(a,b):
    if a>b:
        return gcd(b,a)
    if a==0:
        return b
    return gcd(b-a*(b//a),a)
def lcm(x,y):
    return (x*y)//gcd(x,y)
N=int(input())
A=list(map(int,input().split()))
s=1
for a in A:
    s=lcm(s,a)
ans=0
for a in A:
    ans+=s//a
print(ans%(10**9+7))