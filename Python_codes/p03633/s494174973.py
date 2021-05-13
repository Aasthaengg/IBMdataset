from math import gcd
n=int(input())
t=[int(input())for i in range(n)]
ans=1
for i in t:ans*=i//(gcd(ans,i))
print(ans)