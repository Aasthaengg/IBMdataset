n=int(input())
mod=10**9+7
a=pow(10,n,mod)
b=pow(9,n,mod)*2
c=pow(8,n)
d=(a-b+c)%mod
print(d)