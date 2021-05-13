N=int(input())

p=10**9+7
pow=1
for i in range(1,N+1):
  pow=pow*i % p

print(pow)