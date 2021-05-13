K,X=input().split()
K=int(K)
X=int(X)
print(*[i+X-K+1 for i in range(2*K-1)])