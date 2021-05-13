K,N=map(int,input().split())
A=list(map(int,input().split()))

dmax = K + A[0] - A[-1]
for i in range(1,N):
    if A[i]-A[i-1] > dmax:
        dmax = A[i]-A[i-1]

print(K-dmax)