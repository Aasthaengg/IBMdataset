K,T=map(int,input().split())
A=list(map(int,input().split()))
A.sort(reverse=True)
print(max(A[0]-1-(K-A[0]),0))