N,M,K=map(int,input().split())
l=[i*j+(N-i)*(M-j) for i in range(N+1) for j in range(M+1)]
print('Yes' if K in l else 'No')