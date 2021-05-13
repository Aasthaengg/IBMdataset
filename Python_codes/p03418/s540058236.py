N, K = map(int, input().split())
print(sum(N//b*(b-K)+max(0,N%b-K+1)-(K==0) for b in range(K+1,N+1)))