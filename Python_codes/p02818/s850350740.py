A, B, K = list(map(int, input().split()))
a = max(A - K, 0)
b = max(B - max((K - A), 0), 0)
print(a, b)
