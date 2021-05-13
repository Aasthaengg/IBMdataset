A=list(map(int,input().split()))
print(sum(A) if A[1]%A[0]==0 else A[1]-A[0])