K,X=map(int,input().split())
if K==1:print(X)
else:print(*list(range(X-K+1,X+K)))