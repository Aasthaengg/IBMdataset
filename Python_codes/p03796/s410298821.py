N=int(input())
mod=10**9+7

factorial=[1 for i in range(N+1)]
for i in range(1,N+1):
    if i==1:factorial[i]=1
    else:factorial[i] = factorial[i-1]*i % mod
      
print(factorial[N])