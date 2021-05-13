N = int(input())
A = sorted([int(X) for X in input().split()],reverse=True)
print(sum(A[::2])-sum(A[1::2]))