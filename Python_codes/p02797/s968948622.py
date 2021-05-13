N,K,S=map(int,input().split())
n=10**9
if S==n: n=1
ans=[S]*K+[n]*(N-K)
print(*ans)