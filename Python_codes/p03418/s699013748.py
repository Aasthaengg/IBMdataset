N,K = map(int,input().split())
ans = sum(N//b*(b-K) + max(0,N%b-K+1) for b in range(K+1,N+1)) if K>0 else N*N
print(ans)