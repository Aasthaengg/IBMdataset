N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sumA = sum(A)
a = A[:]
for i, b in enumerate(B):
    if a[i] < b:
        b -= a[i]
        a[i] = 0
        a[i+1] = max(0, a[i+1] - b)
    else:
        a[i] -= b
ans = sumA - sum(a)
a = A[:]
for i in range(N - 1, -1, -1):
    b = B[i]
    if a[i+1] < b:
        b -= a[i+1]
        a[i+1] = 0
        a[i] = max(0, a[i] - b)
    else:
        a[i+1] -= b
ans = max(ans, sumA - sum(a))
print(ans)