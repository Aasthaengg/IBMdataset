N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
A.reverse()
if A[M - 1] * 4 * M < sum(A):
    print("No")
else:
    print("Yes")