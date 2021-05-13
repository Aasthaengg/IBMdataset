N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
sumA = sum(A)

for i, b in enumerate(B):
    c = min(A[i], b)
    A[i] -= c
    A[i + 1] -= min(A[i + 1], b - c)

print(sumA - sum(A))