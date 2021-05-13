a = list(map(int,input().split()))
A = sorted(a,reverse = True)
print(abs(A[1]-A[0]) + abs(A[2] - A[1]))