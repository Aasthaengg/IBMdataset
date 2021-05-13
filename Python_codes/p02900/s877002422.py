a,b=map(int,input().split())
import math

d=math.gcd(a,b)

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
  
r=make_divisors(d)
l=len(r)
ans=1
w=[True]*l
if l>=2:
  for x in range(1,l):
    if w[x]==True:
      ans+=1
      for y in range(x,l):
        if r[y]%r[x]==0:
          w[y]=False
          
print(ans)