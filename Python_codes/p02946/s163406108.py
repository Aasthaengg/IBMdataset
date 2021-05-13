K,X = map(int,input().split())

for i in range(max(-1000000,X-K+1), min(X+K,1000000)):
    print(i, end=' ')
