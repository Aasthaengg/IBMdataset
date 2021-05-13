N, M = list(map(lambda x: int(x), input().split(" ")))
A = list(map(lambda y: int(y), input().split(" ")))
A.sort(reverse=True)
 
print("Yes") if 0.25 * sum(A) / M <= A[M - 1] else print("No")