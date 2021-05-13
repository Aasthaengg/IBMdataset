M,K=map(int,input().split())
x=list(range(2**M))
print(*x[::-1]+x if K==0 else x[:K:-1]+x[K-1::-1]+[K]+x[:K]+x[K+1:]+[K] if K<2**M and M>1 else[-1])