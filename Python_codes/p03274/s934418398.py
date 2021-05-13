N,K=map(int,input().split())
X=list(map(int,input().split()))
print(min(min(abs(X[i])+abs(X[i+K-1]-X[i]),abs(X[i+K-1])+abs(X[i]-X[i+K-1])) for i in range(N-K+1)))