N,X = (int(X) for X in input().split())
M = [int(input()) for X in range(0,N)]
print(N+(X-sum(M))//min(M))