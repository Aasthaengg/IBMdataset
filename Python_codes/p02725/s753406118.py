K,N=map(int,input().split())
A=list(map(int,input().split()))
M=[A[0]+K-A[N-1]]
for i in range(1,N):
    M.append(A[i]-A[i-1])
M=sorted(M)
print(K-M[N-1])