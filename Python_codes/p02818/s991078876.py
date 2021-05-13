A, B, K = map(int, input().split())
if K <= A:
    a = A - K
    b = B
else:
    a = 0
    b = max(0, B - (K-A))
print(a, b)