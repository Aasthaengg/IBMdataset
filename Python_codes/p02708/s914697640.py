N,K=map(int,input().split())
print((((K-N-2)*(2*K*K-K*(N+2)-N*(N+1)))//6+N+2-K)%(10**9+7))