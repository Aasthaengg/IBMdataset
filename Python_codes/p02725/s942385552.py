K,N=map(int,input().split())
*A,=sorted(map(int,input().split()))
print(K-max([*[A[i+1]-A[i] for i in range(N-1)], A[0]+(K-A[-1])]))