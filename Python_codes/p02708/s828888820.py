import math
N,K=map(int,input().split())

A=[i for i in range(N+1)]
wa=0
N=N+1
for i in range(K,N+1):

    mi=(i*(0+(i-1)))/(2)
    ma=(i*(N-i+(N-1)))/(2)

    wa=ma-mi+1+wa


wa=wa%(10**9+7)
print(int(wa))
