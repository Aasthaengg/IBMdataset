A = list(map(int,input().split()))
A.sort()
A[2]=A[2]*10
print(sum(A))