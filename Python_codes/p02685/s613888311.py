N,M,K = map(int, input().split())

p = 998244353

factorial = [1]
counter = 0
for i in range(1,N+1):
    factorial.append(factorial[i-1]*i%p)



for k in range(K+1):
    counter += factorial[N-1]*pow(factorial[k],p-2,p)*pow(factorial[N-k-1],p-2,p)*M*pow(M-1,N-1-k,p)
print(counter%p)
