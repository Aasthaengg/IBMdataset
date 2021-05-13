A=list(map(int,input().split()))
A.sort(key=int)
print((A[1]-A[0])+(A[2]-A[1]))