K,X = map(int,input().split())
print(*(list(range(X-K+1,X))+list(range(X,X+K))))