A1, A2, A3 = map(int, input().split())

A = [A1, A2, A3]

A.sort()

cst1 = A[2] - A[1]

cst2 = A[1] - A[0]

cst = cst1 + cst2

print(cst)