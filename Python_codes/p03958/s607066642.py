k, t = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
max_value = A[-1]
others = sum(A[:-1])
print(max(0, max_value - others - 1))