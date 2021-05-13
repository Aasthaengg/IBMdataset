N,K,X,Y = [int(input()) for _ in range(4)]
print(N*X-(X-Y)*max(N-K,0))