N,K=map(int,input().split())
print(sum([(max((i-K),0)*(N//i)+max(N%i-K+min(K,1),0)) for i in range(1,N+1)]))