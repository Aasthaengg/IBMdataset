K, X = list(map(int,input().rstrip().split()))
print(*[i for i in range(X-K+1,X+K)])