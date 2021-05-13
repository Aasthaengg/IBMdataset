from math import gcd
n=int(input())
v=list(map(int,input().split()))
v.sort()
ans=v[0]/(2**(n-1))
div=2**n
for i in range(1,n):
    div/=2
    ans+=v[i]/div

print(ans)