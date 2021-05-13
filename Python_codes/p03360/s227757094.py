A=list(map(int,input().split()))
K = int(input())
A.sort()
print(A[2] * 2**K + A[0] + A[1])
