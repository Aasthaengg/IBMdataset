N,K=map(int,input().split())
A=list(map(int,input().split()))
N=N-1
K=K-1
if N==K:
    print(1)
    exit()
if N%K==0:
    print(N//K)
else:
    print(N//K+1)