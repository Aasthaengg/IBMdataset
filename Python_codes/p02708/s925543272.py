N,K = map(int,input().split())
count = 0
for i in range(K,N+2):
    lb = 0.5*i*(i-1)
    ub = i*N-lb
    b = ub-lb+1
    #print(ub,lb,b)
    count += b
    count %= 10**9+7
print(int(count))