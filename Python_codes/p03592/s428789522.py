N,M,K=map(int, input().split())
print("YNeos"[not any(K==i*j+(N-i)*(M-j) for i in range(N+1) for j in range(M+1))::2])