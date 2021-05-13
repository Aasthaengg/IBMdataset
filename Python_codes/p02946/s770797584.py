X, K = map(int, input().split())

if X == 1:
    print(K)
else:
    for i in range(K - X +1,K + X):
        print(i,end=" ")