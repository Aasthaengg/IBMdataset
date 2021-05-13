K,X=map(int,input().split())
for i in range(K):
    if -1000000<X-K+1+i<=1000000:
        print(X-K+1+i,end=" ")
for j in range(K-1):
    if -1000000<X+1+j<=1000000:
        print(X+1+j,end=" ")