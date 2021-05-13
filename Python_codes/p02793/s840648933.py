def gcd(n,m):
  if n>m:
    return gcd(m,n);
  if n==0:
    return m;
  return gcd(m-n*(m//n),n)

def lcm(x, y):
    return (x * y) // gcd(x, y)
  
n=int(input())
a=list(map(int,input().split()))
s=1
for i in a:
  s=lcm(s,i)
ans=0
for i in a:
  ans+=s//i
print(ans % 1000000007)