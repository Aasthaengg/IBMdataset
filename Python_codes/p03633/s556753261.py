from math import gcd
def lcm(x,y):
    return (x*y)//gcd(x,y)
N=int(input())
ans=1
for i in range(N):
    ans=lcm(ans,int(input()))
print(ans)
