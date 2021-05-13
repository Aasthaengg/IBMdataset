n = int(input())
A, B = [], []
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

A.sort()
B.sort()

res = 0

if n % 2 == 1:
    midA = A[n // 2]
    midB = B[n // 2]
    if midB >= midA:
        res = midB - midA + 1
    else:
        res = 0
else:
    midA = A[n // 2 - 1] + A[n // 2] 
    midB = B[n // 2 - 1] + B[n // 2]
    if midB >= midA:
        res = midB - midA + 1
    else:
        res = 0
print(res)