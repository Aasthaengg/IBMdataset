n, *A = map(int, open(0).read().split())
A.sort()
print(A[-1], min(A, key=lambda x:abs(2*x-A[-1])))