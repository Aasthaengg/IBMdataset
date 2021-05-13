n=int(input())
mod=10**9+7
x=pow(10,n,mod)
y=pow(9,n,mod)
z=pow(8,n,mod)
print((x-2*y+z)%mod)