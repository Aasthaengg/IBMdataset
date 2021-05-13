K, X = map(int, input().split())

for i in range(X-K+1, X+K):
    if i == X+K-1:
        print(i)
    else:
        print(i, end=" ")
