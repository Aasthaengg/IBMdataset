N,M=map(int,input().split())
if 2*N>=M:
    print(M//2)
if 2*N<M:
    L=M-2*N
    print(N+L//4)