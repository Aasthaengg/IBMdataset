N,K = map(int,input().split())
A = list(map(int,input().split()))
if N == K:
    print(1)
else:
    print((N+K-3)//(K-1))