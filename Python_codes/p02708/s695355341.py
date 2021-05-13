p = 10**9+7
N,K = map(int,input().split())
a = (((N+1)*(N+2))//2)%p
a = (a*(N+1))%p
b = (((K-1)*K)//2)%p
b = (b*(N+1))%p
c = (((N+1)*(N+2)*(2*N+3))//6)%p
d = (((K-1)*K*(2*K-1))//6)%p
e = (N-K+2)%p
ans = (a-b-c+d+e)%p
print(ans)