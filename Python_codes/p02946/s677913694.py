K,X = map(int,input().split())

for i in range(X-K+1, X+K):
    if -1000000<=i<=1000000:
        print(i, end=' ')
