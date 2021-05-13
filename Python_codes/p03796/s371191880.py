n = int(input())
prod=1
mod=1000000007
for i in range(1,n+1):
  prod = ((prod%mod)*(i%mod))%mod

print(prod)