N=int(input())
def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)
def lcm(x,y):
    return x*y//gcd(x,y)
ans=1
for _ in range(N):
  T=int(input())
  ans=lcm(ans,T)
print(ans)