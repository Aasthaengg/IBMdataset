import math
n,m=map(int,input().split())
s=list(input())
t=list(input())
num=math.gcd(n,m)
ans=(n*m)//num
numn=n//num
numm=m//num
for i in range(num):
    if s[i*numn]!=t[i*numm]:
        ans=-1
        break
print(ans)
