N, M = map(int,input().split())
X = (N-M)*100*(2**M) + M*1900*(2**M)
print(X)